variable "ssh_public_key" {
  description = "Your SSH public key (~/.ssh/id_ed25519.pub)"
  type        = string
  sensitive   = true
}