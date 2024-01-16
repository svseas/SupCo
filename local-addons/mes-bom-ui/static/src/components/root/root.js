/** @odoo-module */
import { registry } from "@web/core/registry";
import { Component, onMounted, xml, onRendered, useEnv } from "@odoo/owl";
import { ContentContainer } from "../content-container/content-container";
import { Navbar } from "../navbar/navbar";
import { navData } from "../navbar/navbar-data";
import { useContentStore } from "./contentStore";
import { BomGetData } from "../mes-get-data/mes-get-data";
import { MainContentCreate } from "../main-content-create/main-content-create";
import { TopContent } from "../top-content/top-content";
import { ActionContainer } from "@web/webclient/actions/action_container";

export class Root extends Component {
  setup() {
    this.contentStore = useContentStore();
    this.env = useEnv();
    this.record = this.props.record;
    onMounted(() => {
      globalThis.contentStore = this.contentStore;
      const header = document.querySelector("header");
      const navbar = document.querySelector(".o_main_navbar");
      const body = document.querySelector("body");
      // add event Listener on keydown K toggle classList d-none
      header.classList.add("d-none");
      header.classList.add("fixed-top");
      const webclient = document.querySelector(".o_web_client");
      navbar.style.background = "#0b6b60";
      webclient.style.display = "block";
    });

    onRendered(() => {
    });
  }

  static components = {
    ContentContainer,
    BomGetData,
    Navbar,
    MainContentCreate,
    TopContent,
    ActionContainer,
  };

  static props = [];
}

Root.template = "mes-bom-ui.root";

registry.category("actions").add("mes-bom-ui.action-root", Root);
