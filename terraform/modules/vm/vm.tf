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
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCz32mPLHmrtnahfYXbtBwJWI1Fz9VjFzXYVskTr6ZOonOq2OL5n+EJGZVaOdPkIxTmmfdKHOL/4mklV7ojqz2467rrOFEKZCltAstvrfqQMa8XbUqtqCzqCvnpGtu0AxpreUogUscwHhzYTqi0EEhxMqaEGiRTXkUfidK+xOXD8hI9KHn5vseWfusF+aDdRq1sFK9KmqW0JC2gZusVYktc6cheT8ubZMWW1RrTKw4AoXBuNJKhNaTNU0Iq48QcWraMRQD5q4rth5V3zChwUWMahi8svHwLd+VvzOaJxlGmOlq9QYdmoyld1GvZkuHaicl+VDcA5YSfDNBWvqFmWgb57HAIg4lgtqMT5P/8ooH+zCroaMWRRgRP9EV6xZck7dg2yChzxe+6JmI2LtOFuliCpIGpC2VlRk0beqjxoEX2hs85Bk/WSUPVbswCXkiSfQua22SUUZrK57WNfEfRG60+5x37kTXRkfh7UtqU1gvg70EdOBMLb79mM4qeqT8IYpE= devopsagent@myLinuxVM"
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
