/** @odoo-module */

import { useService } from "@web/core/utils/hooks";

import {
  Component,
  useState,
  onWillStart,
  onWillUpdateProps,
  onMounted,
} from "@odoo/owl";
import { Layout } from "@web/search/layout";

export class LogController extends Component {
  setup() {
    this.orm = useService("orm");
    this.now = new Date().toLocaleString("vi");
    this.model = useState(
      new this.props.Model(
        this.orm,
        this.props.resModel,
        this.props.archInfo,
        this.props.domain
      )
    );
    onWillStart(async () => {
      await this.model.load();
    });

    onWillUpdateProps(async (nextProps) => {
      if (
        JSON.stringify(nextProps.domain) !== JSON.stringify(this.props.domain)
      ) {
        this.model.domain = nextProps.domain;
        await this.model.load();
      }
    });

  }
}

LogController.template = "log_view.LogView";
LogController.components = { Layout };
