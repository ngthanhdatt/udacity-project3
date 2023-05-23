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
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDR/3BY1ARQ8wJRig77nBKREG5adObi4gBBDjUYavSqYAkEFBqy0UzdQpXLpzP6jMkNsTVm8deT4PxVSom/k7J/ZSXTth8/T+rjrxj7p+3kW5Qo212uBNH5y0yaYUO/TQE5LpI7/LBkRcCip3Y8OtmNCo/vxWXQSY+d+cgXgbRefdyxtKImcoyB/viDHbBX6iNQN80HQOuqiWgw8lYu7wPG7Juzoxa7E4+UIxqgD8zcOokMgaeD2YfsRvbZWbE8xS4sPPT26vRtzXWuV2qQ72o32qXAzNuEHt1B+DDcMCN92RqyBPsUp0qfSPahCITgR2z8aReOOTqYzp4a5pe89w4pK7jST4iAyPUOGkvRD0+z8Q3cDvsSwYPKrO9caJKrnnqQ59Nh3GQu29lXEIa9k8e6sbsXByRW9sWPxY2ZSAZtqSj1BmQ684ZNcTR8AV7RB2iww7mulDt8eBoH4xsgKAdipMWLVBMmFB3aqwWcOjUv76Bm9/7o517qhW2reHTZtEk= devopsagent@myLinuxVM"
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
