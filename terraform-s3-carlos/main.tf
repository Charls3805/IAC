terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "carlos_bucket" {
  bucket = "carlos3805-terraform-bucket"
  tags = {
    Name = "CarlosBucketTerraform"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.carlos_bucket.bucket
}