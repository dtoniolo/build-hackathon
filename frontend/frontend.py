import json
from typing import Any

import reflex as rx
import requests
from commons import FormData, SubmissionState
from pydantic import BaseModel


app = rx.App()


class FormState(rx.State):
    form_data: dict[str, Any] = {}
    submission_state: SubmissionState = SubmissionState.FINALIZED

    @rx.event
    def set_submission_state(self, checked: bool) -> None:
        if checked:
            self.submission_state = SubmissionState.FINALIZED
        else:
            self.submission_state = SubmissionState.DRAFT

    @rx.event
    def handle_submit(self, form_data: dict[str, Any]) -> None:
        # Empty fields in an HTML form are modeled with an empty string, which has to be converted to `None`
        for field_name in form_data:
            value = form_data[field_name]
            if value == "":
                form_data[field_name] = None
        parsed_form_data = FormData.parse_obj(form_data)
        obj = {
            "form_data": parsed_form_data.model_dump(),
            "state": self.submission_state.value,
        }
        try:
            response = requests.post(
                "http://127.0.0.1:8001/startup-report/", data=json.dumps(obj)
            )
            if response.status_code != 200:
                raise RuntimeError(
                    f"The server refused the submission. Status code: {response.status_code}, error message: {response.text}."
                )
        except Exception as e:
            raise RuntimeError("Couldn't submit the form.") from e


class FormField(BaseModel):
    field_name: str
    """The name of the field, as defined in `FormData`.

    It will be used also for the HTML `name` of the input.

    """

    type: str
    """The HTML `type` of the button."""

    placeholder: str
    """The placeholder of the button."""

    label: str

    def render(self) -> rx.Component:
        return rx.form.field(
            rx.form.label(self.label),
            rx.tooltip(
                rx.form.control(
                    rx.input(
                        name=self.field_name,
                        type=self.type,
                        placeholder=self.placeholder,
                    ),
                    as_child=True,
                ),
                content=FormData.schema()["properties"][self.field_name]["description"],
            ),
            key=self.field_name,
        )


@app.add_page
def index() -> rx.Component:
    form_fields = [
        FormField(
            field_name="arr",
            type="number",
            placeholder="1234.56",
            label="Annual Recurring Revenue",
        ),
        FormField(
            field_name="number_of_clients",
            type="number",
            placeholder="150",
            label="Number of Clients",
        ),
        FormField(
            field_name="leads_generated",
            type="number",
            placeholder="45",
            label="Leads Generated",
        ),
        FormField(
            field_name="revenue",
            type="number",
            placeholder="500,000.00",
            label="Revenue (Last 12 Months)",
        ),
        FormField(
            field_name="ebitda",
            type="number",
            placeholder="75,000.00",
            label="EBITDA (Last 12 Months)",
        ),
        FormField(
            field_name="ebit",
            type="number",
            placeholder="65,000.00",
            label="EBIT (Last 12 Months)",
        ),
        FormField(
            field_name="corporate_tax",
            type="number",
            placeholder="15,000.00",
            label="Corporate Tax (Last 12 Months)",
        ),
        FormField(
            field_name="total_assets",
            type="number",
            placeholder="10,000.00",
            label="Total Assets",
        ),
        FormField(
            field_name="intangible_assets",
            type="number",
            placeholder="2,500.00",
            label="Intangible Assets",
        ),
        FormField(
            field_name="debt",
            type="number",
            placeholder="0.00",
            label="Debt",
        ),
        FormField(
            field_name="debt_to_ebitda",
            type="number",
            placeholder="2.5",
            label="Debt to EBITDA Ratio",
        ),
        FormField(
            field_name="percent_international_sales",
            type="number",
            placeholder="35.5",
            label="International Sales (%)",
        ),
        FormField(
            field_name="number_of_employees",
            type="number",
            placeholder="25",
            label="Number of Employees",
        ),
        FormField(
            field_name="number_of_female_employees",
            type="number",
            placeholder="12",
            label="Number of Female Employees",
        ),
        FormField(
            field_name="number_of_c_level_executives",
            type="number",
            placeholder="3",
            label="Number of C-Level Executives",
        ),
        FormField(
            field_name="number_of_female_c_level_executives",
            type="number",
            placeholder="1",
            label="Number of Female C-Level Executives",
        ),
        FormField(
            field_name="number_of_board_members",
            type="number",
            placeholder="5",
            label="Number of Board Members",
        ),
        FormField(
            field_name="number_of_female_board_members",
            type="number",
            placeholder="2",
            label="Number of Female Board Members",
        ),
        FormField(
            field_name="monthly_burn",
            type="number",
            placeholder="25000.00",
            label="Monthly Burn Rate",
        ),
        FormField(
            field_name="runway_months",
            type="number",
            placeholder="18.5",
            label="Runway (Months)",
        ),
        FormField(
            field_name="gross_margin_percent",
            type="number",
            placeholder="75.0",
            label="Gross Margin (%)",
        ),
        FormField(
            field_name="annual_logo_churn_percent",
            type="number",
            placeholder="5.2",
            label="Annual Logo Churn (%)",
        ),
        FormField(
            field_name="annual_revenue_churn_percent",
            type="number",
            placeholder="8.1",
            label="Annual Revenue Churn (%)",
        ),
        FormField(
            field_name="net_revenue_retention_percent",
            type="number",
            placeholder="110.5",
            label="Net Revenue Retention (%)",
        ),
        FormField(
            field_name="average_acv",
            type="number",
            placeholder="12000.00",
            label="Average Annual Contract Value",
        ),
        FormField(
            field_name="payback_months",
            type="number",
            placeholder="14.2",
            label="CAC Payback Period (Months)",
        ),
        FormField(
            field_name="sales_and_marketing_expenses_percent_of_revenue",
            type="number",
            placeholder="25.5",
            label="Sales & Marketing Expenses (% of Revenue)",
        ),
        FormField(
            field_name="general_and_administration_expenses_percent_of_revenue",
            type="number",
            placeholder="12.3",
            label="General & Admin Expenses (% of Revenue)",
        ),
        FormField(
            field_name="research_and_development_expenses_percent_of_revenue",
            type="number",
            placeholder="18.7",
            label="R&D Expenses (% of Revenue)",
        ),
    ]
    return rx.center(
        rx.form.root(
            rx.heading("Quarterly Metrics Update"),
            list(map(lambda field: field.render(), form_fields)),
            rx.flex(
                rx.switch(
                    checked=FormState.submission_state == SubmissionState.FINALIZED,
                    on_change=FormState.set_submission_state,
                ),
                rx.cond(
                    FormState.submission_state == SubmissionState.FINALIZED,
                    rx.button("Submit", type="submit"),
                    rx.button("Save Draft", type="submit"),
                ),
                flex_direction="row",
                justify_content="flex-end",
                align_items="center",
                gap="15px",
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
            max_width="500px",
            height="100%",
            flex_direction="column",
            align_content="center",
            row_gap="100px",
        ),
        height="100vh",
    )
