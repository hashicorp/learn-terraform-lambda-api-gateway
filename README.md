# Serverless REST API

0. Install Terraform

    1. Download from https://www.terraform.io/downloads.html
    2. Unzip in Downloads such that `~/Downloads/terraform` exists
    3. Move to path: `mv ~/Downloads/terraform /usr/local/bin/`
    4. Verify installation
        ```
        $ terraform -v

        Terraform v1.0.3
        on darwin_amd64
        + provider registry.terraform.io/hashicorp/archive v2.2.0
        + provider registry.terraform.io/hashicorp/aws v3.48.0
        + provider registry.terraform.io/hashicorp/random v3.1.0
        ```

1. Initialize Terraform, download providers

    ```
    terraform init
    ```

2. Preview resource creation

    ```
    terraform plan
    ```

3. Create resources

    ```
    terraform apply
    ```