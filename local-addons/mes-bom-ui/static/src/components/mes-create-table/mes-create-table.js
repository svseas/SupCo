/**@odoo-module */
import { Component, onMounted, onRendered } from "@odoo/owl";
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesButton } from "../mes-button/mes-button";

export class MesCreateTable extends Component {
  setup() {
    super.setup(...arguments);
    this.dataTable = this.props.data;
    onRendered(() => {
    })
  }

  static props = {
    data: { type: Object, optional: true },
  };

  static components = {
    MesButton,
  };
  static defaultProps = {
    data: {
      data: [],
      keys: {
        'code': "MÃ",
        'name': "SẢN PHẨM",
        'description': "CHI TIẾT",
        'sequence': "TRẠNG THÁI",
      }
    }
  }

}
MesCreateTable.template = "mes-bom-ui.mes_create_table_template";