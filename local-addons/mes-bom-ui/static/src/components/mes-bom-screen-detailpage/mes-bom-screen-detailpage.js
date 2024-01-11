/**@odoo-module */
import { Component, onWillUpdateProps, useState, onRendered } from "@odoo/owl";
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesTabButton } from "../mes-tab-button/mes-tab-button";
import { MesCreateTable } from "../mes-create-table/mes-create-table";

export class MesBomDetailPage extends Component {
  setup() {
    super.setup(...arguments);
    onRendered(() => {
    })
    this.currentTab = useState({
      name: 'quytrinh',
    })
    this.data = this.props.data
  }
  static components = {
    MesTabButton,
    MesCreateTable,
  }
  static props = {
    data: { type: Object, optional: true },
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
  setCurrentTab(tabName) {
    this.currentTab.name = tabName
  }
}
MesBomDetailPage.template = "mes-bom-ui.mes_bom_detail_page_template";