/** @odoo-module */
const { Component } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require("web.rpc");
import { WebClient } from "@web/webclient/webclient";
import { Navbar } from "../navbar/navbar";
import { TopContent } from "../top-content/top-content";
import { Root } from "../root/root";

export class MyWebClient extends Component {}
MyWebClient.components = {
  Navbar,
};
MyWebClient.template = "web.MyWebClient";
Object.assign(WebClient.components, { Navbar, TopContent, Root });
