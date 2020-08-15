from adminapp.controllers import AdminPanel, CreateCourse, CreateCategory

ADMIN_ROUTES = {
    '/admin/': AdminPanel(),
    '/admin/new_course/': CreateCourse(),
    '/admin/new_category/': CreateCategory(),
}
