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

2. Configure AWS Credentials at `~/.aws/credentials`

    ```
    cat ~/.aws/credentials
    [default]
    aws_access_key_id=<secret>
    aws_secret_access_key=<secret>
    ```

3. Preview resource creation

    ```
    terraform plan
    ```

4. Create resources

    ```
    terraform apply
    ```

5. Observe outputs when creation is finished form the `apply` command

    ```
    Apply complete! Resources: 0 added, 2 changed, 0 destroyed.

    Outputs:

    base_url = "https://effixq4jwb.execute-api.us-east-1.amazonaws.com/serverless_lambda_stage"
    function_name = "serverless-rest-api"
    lambda_bucket_name = "learn-terraform-functions-roughly-explicitly-live-ferret"
    ```

6. Check your REST Endpoint
    
    ```
    curl "$(terraform output -raw base_url)/hello"
    ```
