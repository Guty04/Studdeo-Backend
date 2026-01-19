from app.repositories import OdooRepository

odoo = OdooRepository().get_courses(teacher_id=8)

print(odoo)
