variable "connector_name" {
  description = "Directory name of the Connector SDK connector"
  type        = string

  validation {
    condition = contains([
      "billing_invoices",
      "crm_contacts",
      "product_events",
      "support_tickets",
    ], var.connector_name)

    error_message = "connector_name must identify one of the four demo connectors."
  }
}

variable "group_id" {
  description = "Fivetran destination group ID"
  type        = string
}

variable "python_version" {
  description = "Python version used by the deployed Connector SDK connector"
  type        = string
  default     = "3.14"
}