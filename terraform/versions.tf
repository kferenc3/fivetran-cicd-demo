terraform {
  required_version = ">= 1.10.0, < 2.0.0"

  cloud {
    organization = "kferenc-test"

    workspaces {
      project = "fivetran-cicd-demo"

      tags = {
        application = "fivetran-cicd-demo"
      }
    }
  }

  required_providers {
    fivetran = {
      source  = "fivetran/fivetran"
      version = "1.9.41"
    }
  }
}