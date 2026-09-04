locals {
  package_file = "${path.module}/../connectors/${var.connector_name}/files/${var.connector_name}.zip"
}

resource "fivetran_connector_sdk_package" "this" {
  file_path = local.package_file
}

resource "fivetran_connector" "this" {
  group_id = var.group_id
  service  = "connector_sdk"

  destination_schema {
    name = var.connector_name
  }

  config {
    package_id     = fivetran_connector_sdk_package.this.id
    python_version = var.python_version
  }

  run_setup_tests = false
}