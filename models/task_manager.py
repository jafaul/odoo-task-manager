from odoo import _, fields, models


class TaskManager(models.Model):
    _name = "task.manager"
    _description = "Task Manager"

    name = fields.Char(_("Task Name"), required=True)
    description = fields.Text(_("Task Description"))
    assigned_to = fields.Many2one("res.users", string=_("Assigned to"))
    due_date = fields.Datetime(_("Due Date"))
    priority = fields.Selection(
        selection=[("low", _("Low")), ("medium", _("Medium")), ("high", _("High"))],
        default="low",
    )
    status = fields.Selection(
        selection=[
            ("new", _("New")),
            ("in_progress", _("In Progress")),
            ("completed", _("Completed")),
        ],
        default="new",
    )

    def days_until_due(self):
        if self.due_date:
            today = fields.Date.today()
            due_date = self.due_date.date()
            delta = (due_date - today).days
            return delta
        return None

    def send_due_soon_notifications(self):
        tasks = self.search([("due_date", "!=", False), ("status", "!=", "completed")])
        for task in tasks:
            days_left = task.days_until_due()
            if days_left is not None and days_left == 3 and task.assigned_to.email:
                template = self.env.ref("task_manager.task_expiry_email_template")
                template.send_mail(task.id, force_send=True)
