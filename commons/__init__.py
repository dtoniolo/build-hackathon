from decimal import Decimal
from enum import Enum, unique
from typing import Optional

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Financial and business metrics for a given reporting period."""

    arr: Optional[Decimal] = Field(
        default=None, description="Annual Recurring Revenue at the end of the quarter."
    )
    number_of_clients: Optional[int] = Field(
        default=None, description="Number of clients at period end."
    )
    leads_generated: Optional[int] = Field(
        default=None, description="Number of leads generated in the period."
    )
    revenue: Optional[Decimal] = Field(
        default=None,
        description="Revenue over the last 12 months (sum of the past 12 months).",
    )
    ebitda: Optional[Decimal] = Field(
        default=None,
        description="EBITDA over the last 12 months (sum of the past 12 months).",
    )
    ebit: Optional[Decimal] = Field(
        default=None,
        description="EBIT over the last 12 months (sum of the past 12 months).",
    )
    corporate_tax: Optional[Decimal] = Field(
        default=None,
        description="Corporate tax over the last 12 months (sum of the past 12 months).",
    )
    total_assets: Optional[Decimal] = Field(
        default=None, description="Total assets at the end of the quarter."
    )
    intangible_assets: Optional[Decimal] = Field(
        default=None, description="Intangible assets at the end of the quarter."
    )
    debt: Optional[Decimal] = Field(
        default=None, description="Debt at the end of the quarter."
    )
    debt_to_ebitda: Optional[float] = Field(
        default=None, description="Debt divided by EBITDA at the end of the quarter."
    )
    percent_international_sales: Optional[float] = Field(
        default=None,
        description="Percentage of sales that are international at the end of the quarter.",
    )
    number_of_employees: Optional[int] = Field(
        default=None, description="Number of employees at period end."
    )
    number_of_female_employees: Optional[int] = Field(
        default=None, description="Number of female employees at period end."
    )
    number_of_c_level_executives: Optional[int] = Field(
        default=None, description="Number of C-level executives at period end."
    )
    number_of_female_c_level_executives: Optional[int] = Field(
        default=None, description="Number of female C-level executives at period end."
    )
    number_of_board_members: Optional[int] = Field(
        default=None, description="Number of board members at period end."
    )
    number_of_female_board_members: Optional[int] = Field(
        default=None, description="Number of female board members at period end."
    )
    monthly_burn: Optional[Decimal] = Field(
        default=None,
        description="Average monthly cash burned in the quarter (cash burned in the quarter / 3).",
    )
    runway_months: Optional[float] = Field(
        default=None,
        description="Cash runway in months (cash in the bank / monthly burn rate).",
    )
    gross_margin_percent: Optional[float] = Field(
        default=None,
        description="Gross margin percentage (last month or average for the quarter).",
    )
    annual_logo_churn_percent: Optional[float] = Field(
        default=None,
        description=(
            "Annual logo churn: number of customers lost (sum of the last 12 months) / "
            "total number of customers (12 months ago) * 100."
        ),
    )
    annual_revenue_churn_percent: Optional[float] = Field(
        default=None,
        description=(
            "Annual revenue churn: total cancelled revenue (sum of the last 12 months) / "
            "total revenue (12 months ago) * 100."
        ),
    )
    net_revenue_retention_percent: Optional[float] = Field(
        default=None,
        description=(
            "Net revenue retention: (Starting MRR 12 months ago + Expansion MRR over last 12 months "
            "– Churn MRR over last 12 months) / Starting MRR (12 months ago)."
        ),
    )
    average_acv: Optional[Decimal] = Field(
        default=None,
        description=(
            "Average annual contract value (total contract value / total number of customers). "
            "If multi-year contracts, consider 1-year contract value (e.g., €1M for 2 years is €0.5M per year)."
        ),
    )
    payback_months: Optional[float] = Field(
        default=None,
        description="Months to recover CAC: CAC / (Average ACV * gross margin / 12).",
    )
    sales_and_marketing_expenses_percent_of_revenue: Optional[float] = Field(
        default=None,
        description="Sales & Marketing expenses as a percentage of total revenue.",
    )
    general_and_administration_expenses_percent_of_revenue: Optional[float] = Field(
        default=None,
        description="General & Administration expenses as a percentage of total revenue.",
    )
    research_and_development_expenses_percent_of_revenue: Optional[float] = Field(
        default=None,
        description="Research & Development expenses as a percentage of total revenue.",
    )


@unique
class SubmissionState(Enum):
    DRAFT = "draft"
    FINALIZED = "finalized"
