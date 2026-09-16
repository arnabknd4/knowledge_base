
# What is Terraform? Get Started With Infrastructure as Code

What is Terraform?
Terraform is an open-source tool that lets you define infrastructure components and their relationships using a high-level configuration language.

In Terraform’s human-readable configuration files, you can specify the desired state of your infrastructure and Terraform automatically works out how to get to that state. These files can be versioned, shared, and reused to provide a consistent way to manage your infrastructure, from compute and storage resources, to DNS and SaaS features.

Terraform can be used with various cloud providers, in multi-cloud infrastructures, and on-premises environments.

Key Features of Terraform
Let’s take a closer look at the fundamental aspects that set Terraform apart: 

HashiCorp Configuration Language
Terraform uses a high-level language called HashiCorp’s Configuration Language (HCL), designed specifically for defining infrastructure as code. High-level configuration languages implement a declarative syntax which is abstract and user-friendly compared to low-level scripting and manual configuration. You might have encountered high-level languages before, in YAML or JSON files. 

HCL follows a block structure, where each nested block represents resources and their configurations. Resources are explicitly defined with names and attributes.

`
resource "aws_instance" "example" {
    ami = "ami-123456"
    instance_type = "t2.micro"
}
`
