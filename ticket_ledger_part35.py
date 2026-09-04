# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TicketLedger
def next_action_recommendations(applications):
    """Generate next-action recommendations based on ticket status and priority."""
    if not applications:
        return []

    recommendations = []
    for app in applications:
        if app['status'] == 'pending' and app['priority'] == 'high':
            recommendations.append(f"Review high-priority pending ticket #{app['id']}")
        elif app['status'] == 'in_progress' and app['deadline'] and app['deadline'] < datetime.now():
            recommendations.append(f"Urgent: Overdue ticket #{app['id']} needs attention")
        elif app['status'] == 'pending' and app['category'] == 'security':
            recommendations.append(f"Investigate security ticket #{app['id']}")
        elif app['status'] == 'in_progress' and app['assignee'] and app['assignee'].get('email'):
            recommendations.append(f"Check progress on ticket #{app['id']} assigned to {app['assignee']['email']}")
    
    return recommendations
