/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require("web.rpc");
import { MesButton } from "../mes-button/mes-button";
import { xml } from "@odoo/owl";

export class MesGetData extends Component {
  setup() {
    super.setup(...arguments);
    this.loading = true;
    this.dataTable = useState({
      data: [],
      keys: [],
    });
  }

  static props = {
    model: { type: String, optional: true },
    method: { type: String, optional: true },
  };

  static components = {
    MesButton,
  };

  loadData(arg) {
    if (this.loading) {
      let self = this;
      const model = arg.model;
      const method = arg.method;
      rpc
        .query({
          model: model,
          method: method,
        })
        .then(function (data) {
          self.dataTable.data = data[0];
          self.dataTable.keys = data[1];
        })
        .catch(function (error) {
          console.error("Error fetching data for ", error);
        });
      this.loading = false;
    }
  }
}
MesGetData.template = "mes-bom-ui.mes_get_data_template";

export class BomGetData extends Component { }

BomGetData.components = { MesGetData, ...MesGetData.components };
BomGetData.template = xml`<MesGetData model="'mrp.bom'" method="'get_bom_data'"></MesGetData>`;
