{
    "name": "Task Manager",
    "author": "A.Olifir",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    "data": [
        "security/ir.model.access.csv",
        "report/report_tasks.xml",
        "report/report_tasks_template.xml",
        "data/ir_cron.xml",
        "views/task_view.xml",
        "views/menu.xml",
    ],
    "application": True,
    "installable": True,
    "depends": ["base", "mail"],
}
