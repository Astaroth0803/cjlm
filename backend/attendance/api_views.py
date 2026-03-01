from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from core.models import Beneficiary, Activity
from .models import AttendanceRecord
from datetime import date

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    today = date.today()
    
    # Basic Stats
    attendances_today = AttendanceRecord.objects.filter(date=today).count()
    active_users = Beneficiary.objects.filter(is_active=True).count()
    
    # Top Activity
    top_activity = Activity.objects.annotate(attendance_count=Count('events__attendances')).order_by('-attendance_count').first()
    
    # Chart Data (Last 7 days attendance)
    # Simple aggregation for chart
    from datetime import timedelta
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    chart_data = []
    
    for day in last_7_days:
        count = AttendanceRecord.objects.filter(date=day).count()
        chart_data.append({
            'date': day.strftime('%d %b'),
            'count': count
        })

    # Top 5 Attendees
    top_attendees_qs = Beneficiary.objects.annotate(
        attendance_count=Count('attendances')
    ).filter(attendance_count__gt=0).order_by('-attendance_count')[:5]
    
    top_attendees = [
        {
            'id': b.id,
            'name': f"{b.first_name} {b.last_name}",
            'ci': b.ci,
            'attendance_count': b.attendance_count
        } for b in top_attendees_qs
    ]

    return Response({
        'attendances_today': attendances_today,
        'active_users': active_users,
        'top_activity_name': top_activity.name if top_activity else 'N/A',
        'chart_data': chart_data,
        'top_attendees': top_attendees
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def attendance_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    start_time = request.GET.get('start_time')  # format HH:MM
    end_time = request.GET.get('end_time')       # format HH:MM
    
    qs = AttendanceRecord.objects.select_related('beneficiary', 'event__activity').all()
    
    if start_date:
        qs = qs.filter(date__gte=start_date)
    if end_date:
        qs = qs.filter(date__lte=end_date)
    if start_time:
        qs = qs.filter(time__gte=start_time)
    if end_time:
        qs = qs.filter(time__lte=end_time)
        
    qs = qs.order_by('-date', '-time')
    
    data = []
    for r in qs:
        data.append({
            'id': r.id,
            'date': r.date.strftime('%Y-%m-%d'),
            'time': r.time.strftime('%H:%M') if r.time else '',
            'beneficiary_name': f"{r.beneficiary.first_name} {r.beneficiary.last_name}",
            'beneficiary_ci': r.beneficiary.ci,
            'activity_name': r.event.activity.name,
            'event_name': r.event.name,
        })
        
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activity_attendance_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    qs = AttendanceRecord.objects.select_related('event__activity').all()
    
    if start_date:
        qs = qs.filter(date__gte=start_date)
    if end_date:
        qs = qs.filter(date__lte=end_date)
        
    # Group by Event (and Activity by string relation context in rendering)
    report_data = qs.values(
        'event__activity__name', 
        'event__name'
    ).annotate(
        attendees=Count('beneficiary', distinct=True)
    ).order_by('-attendees')
    
    data = []
    for r in report_data:
        data.append({
            'activity_name': r['event__activity__name'],
            'event_name': r['event__name'],
            'attendees': r['attendees']
        })
        
    return Response(data)

from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beneficiary_profile_report(request, pk):
    b = get_object_or_404(Beneficiary, pk=pk)
    
    total_attendance = AttendanceRecord.objects.filter(beneficiary=b).count()
    
    # Breakdown by activity/event
    activities_data = AttendanceRecord.objects.filter(beneficiary=b).values(
        'event__activity__name', 'event__name'
    ).annotate(
        count=Count('id')
    ).order_by('-count')
    
    recent_attendances = AttendanceRecord.objects.filter(beneficiary=b).select_related('event__activity').order_by('-date')[:5]
    
    recent_list = []
    for r in recent_attendances:
        recent_list.append({
            'date': r.date.strftime('%Y-%m-%d'),
            'activity': r.event.activity.name,
            'event': r.event.name
        })
        
    activity_list = []
    for a in activities_data:
        activity_list.append({
            'activity_name': a['event__activity__name'],
            'event_name': a['event__name'],
            'count': a['count']
        })
    
    profile_data = {
        'id': b.id,
        'first_name': b.first_name,
        'last_name': b.last_name,
        'ci': b.ci,
        'dob': b.dob.strftime('%Y-%m-%d') if b.dob else None,
        'sex': b.get_sex_display(),
        'sector': b.sector,
        'is_active': b.is_active,
        'created_at': b.created_at.strftime('%Y-%m-%d'),
        
        'stats': {
            'total_attendance': total_attendance,
            'top_activities': activity_list,
            'recent_history': recent_list
        }
    }
    
    return Response(profile_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activity_profile_report(request, pk):
    act = get_object_or_404(Activity, pk=pk)
    
    events_qs = act.events.annotate(attendance_count=Count('attendances')).order_by('-id')
    events_list = []
    
    total_attendance = 0
    for e in events_qs:
        events_list.append({
            'id': e.id,
            'name': e.name,
            'date': e.date.strftime('%Y-%m-%d') if e.date else None,
            'attendance_count': e.attendance_count
        })
        total_attendance += e.attendance_count

    profile_data = {
        'id': act.id,
        'name': act.name,
        'category': act.category,
        'deadline_date': act.deadline_date.strftime('%Y-%m-%d') if act.deadline_date else None,
        'description': act.description,
        'is_active': act.is_active,
        'image': act.image,
        'events': events_list,
        'total_attendance': total_attendance
    }
    
    return Response(profile_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def event_attendees_detail(request):
    """
    Returns the list of unique attendees for a given activity+event within a date range.
    Query params: activity_name, event_name, start_date, end_date
    """
    activity_name = request.GET.get('activity_name', '')
    event_name = request.GET.get('event_name', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    qs = AttendanceRecord.objects.select_related('beneficiary', 'event__activity').all()

    if activity_name:
        qs = qs.filter(event__activity__name=activity_name)
    if event_name:
        qs = qs.filter(event__name=event_name)
    if start_date:
        qs = qs.filter(date__gte=start_date)
    if end_date:
        qs = qs.filter(date__lte=end_date)

    qs = qs.order_by('beneficiary__first_name', 'beneficiary__last_name')

    # Unique attendees: one row per beneficiary (most recent attendance date shown)
    seen = {}
    for r in qs:
        bid = r.beneficiary.id
        if bid not in seen:
            seen[bid] = {
                'nombre': f"{r.beneficiary.first_name} {r.beneficiary.last_name}",
                'cedula': r.beneficiary.ci or '-',
                'sector': r.beneficiary.sector or '-',
                'ultima_asistencia': r.date.strftime('%Y-%m-%d'),
                'ultima_hora': r.time.strftime('%H:%M') if r.time else '',
                'total_visitas': 0,
            }
        seen[bid]['total_visitas'] += 1
        # keep the most recent date
        if r.date.strftime('%Y-%m-%d') > seen[bid]['ultima_asistencia']:
            seen[bid]['ultima_asistencia'] = r.date.strftime('%Y-%m-%d')
            seen[bid]['ultima_hora'] = r.time.strftime('%H:%M') if r.time else ''

    return Response(list(seen.values()))

