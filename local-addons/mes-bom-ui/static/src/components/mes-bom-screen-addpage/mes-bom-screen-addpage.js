/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesButton } from "../mes-button/mes-button";
import { MesInput } from "../mes-input/mes-input";
import { MesBomDetailPage } from "../mes-bom-screen-detailpage/mes-bom-screen-detailpage";
import { useService } from "@web/core/utils/hooks";
import { onWillUpdateProps } from "@odoo/owl";

export class MesBomAddPage extends Component {
  setup() {
    super.setup(...arguments);
    this.orm = useService("orm");
    this.data = useState({
      data: [],
      tableData: {
        data: [],
        keys: [],
      },
      inputValue: {
        name: '',
        ng: '',
        createdName: '',
        approvedName: '',
      },
      isShowLi: false,
    })
  }
  static components = {
    MesInput,
    MesButton,
    MesBomDetailPage,
  }
  async loadBom() {
    const bom = await this.orm.searchRead(
      "mrp.bom",
      [],
      ["product_tmpl_id", "tech_process_ids", "ng_percent", "created_by", "approved_by", "bom_uom"]
    );
    this.data.data = bom;
    this.data.isShowLi = true;
  }
  async loadTable() {
    const techProcessIds = this.data.data[0].tech_process_ids
    const tableData = await this.orm.searchRead(
      "tech.process",
      [["id", "in", techProcessIds]],
      ["name", "code", "description", "sequence"]
    );
    const keys = {
      'code': "MÃ",
      'name': "SẢN PHẨM",
      'description': "CHI TIẾT",
      'sequence': "TRẠNG THÁI",
    };
    return {
      tableData, keys,
    }
    this.data.tableData.data = tableData;
    this.data.tableData.keys = keys;

  };
  async getInputValue(item) {
    const res = await this.loadTable();
    this.data.tableData.data = res.tableData;
    this.data.tableData.keys = res.keys;
    this.data.inputValue.name = item.product_tmpl_id[1];
    this.data.inputValue.approvedName = item.approved_by[1];
    this.data.inputValue.createdName = item.created_by[1];
    this.data.inputValue.ng = item.ng_percent;
    this.render();
  }
}
MesBomAddPage.template = "mes-bom-ui.mes_bom_add_page_template";