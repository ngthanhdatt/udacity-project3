resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  admin_password      = "${var.admin_password}"
  disable_password_authentication = false
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDdVGMxf9GJPT9qcV73LDhAJeZjB7X7gO2Ko+tgBBdiU8WzHef467JcODbaFqwUGhIwdtigjY5rS1QA5jCaOAu2lJrVdPtGe8b+jAFKz/PaoRJOmhVZ8iBsekell2c73ZjhrDBpxEANGeouinFVQR8pIhYZjrxcp9l1KOQZ7HdqdS+ydsS7J3D2enkAxtE6bGiHO+kw7EPFyF+9q7RNcKWZI9g6dWx2eQrTv7/9UV6VYb4mnguKq0WvZWM4fsT7vazGdKecIyBx+eliFaLkFulog5AU+ZaOawbVRp22DklsnfRbDhNDY86/IC30iXBOInfNPDKJDTD2AsEOTmUCqIxIXTCJ6ODtV+WuXofYY++b0Fr3iwrvMOov6KbUCBOgcIuQt1oe+dP9EBN4bMK9s2OwN/hRbZ2wenWtUErqcW4/qjVEmfeJEYUfEaN4fHXHcbEmMM9wshiuZZxZkhkC6qwJFP2CMV5oNh+dzWA+7U477raTGOIjLb9TZCoAJCVcYcc= devopsagent@myLinuxVM"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
