version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "todo-list-aws"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-ksjl50lc0ea0"
s3_prefix = "todo-list-aws"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
parameter_overrides = "Stage=\"default\""
image_repositories = []

[default]
[default.deploy]
[default.deploy.parameters]
stack_name = "default"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-ksjl50lc0ea0"
s3_prefix = "default"
region = "us-east-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
parameter_overrides = "Stage=\"default\""
image_repositories = []
