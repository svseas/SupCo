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
    // rpc.query({
    //   model: 'material.material',
    //   method: 'get_material_data',
    // }).then(function (data) {
    //   self.dataTable.data = data[0];
    //   self.dataTable.keys = data[1];
    //   console.log("Data=============: ", data)
    // }).catch(function (error) {
    //   console.error('Error fetching data for ', error);
    // });
  }
  newPage() {
    console.log(globalThis.contentStore);
    this.contentStore = globalThis.contentStore;
    this.contentStore.changeContent(MainContentCreate);
  }
}
MainContent.template = "mes-bom-ui.main_content_template";
