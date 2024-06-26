from django.urls import path

from accountants.views import (
    create_accountant_view,
    delete_accountant_view,
    list_accountants_view,
    replace_accountant_view,
)

app_name = "accountants"
urlpatterns = [
    path(
        "<int:company_id>/accountants/", list_accountants_view, name="list_accountants"
    ),
    path(
        "<int:company_id>/accountant/create/",
        create_accountant_view,
        name="create_accountant",
    ),
    path(
        "accountant/replace/<int:accountant_id>/",
        replace_accountant_view,
        name="replace_accountant",
    ),
    path(
        "accountant/delete/<int:accountant_id>/",
        delete_accountant_view,
        name="delete_accountant",
    ),
]
