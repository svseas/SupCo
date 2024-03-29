/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require("web.rpc");
import { MesButton } from "../mes-button/mes-button";
import { MesInput } from "../mes-input/mes-input";
import { MainContentCreate } from "../main-content-create/main-content-create";
export class MainContent extends Component {
  setup() {
    super.setup(...arguments);
    onMounted(() => {
      this.loadData();
    });
    this.dataTable = useState({
      data: [],
      keys: [],
      dict: [],
    });
  }
  static components = {
    MesInput,
    MesButton,
  };
  loadData() {
    let self = this;

  }
  newPage() {

    this.contentStore = globalThis.contentStore;
    this.contentStore.changeContent(MainContentCreate);
  }
}
MainContent.template = "mes-bom-ui.main_content_template";
