output "connector_id" {
  description = "ID of the deployed Fivetran connector"
  value       = fivetran_connector.this.id
}

output "package_id" {
  description = "ID of the uploaded Connector SDK package"
  value       = fivetran_connector_sdk_package.this.id
}