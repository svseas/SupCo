/** @odoo-module */
import { Component } from "@odoo/owl";
import { Navbar } from "../../navbar/navbar";

export class TestNavbar extends Component { }

TestNavbar.components = {
  Navbar,
};
TestNavbar.template = "mes-bom-ui.test-navbar";
