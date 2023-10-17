/** @odoo-module */
import { Component } from "@odoo/owl";
import { TopContent } from "../top-content/top-content";
import { MesBomMainPage } from "../mes-bom-screen-mainpage/mes-bom-screen-mainpage";

export class ContentContainer extends Component {
  static components = {
    TopContent,
    MesBomMainPage,

  };
}

ContentContainer.template = "mes-bom-ui.content_container_template";