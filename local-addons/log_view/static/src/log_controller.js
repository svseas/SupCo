/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { KeepLast } from "@web/core/utils/concurrency";
import { Component, useState, onWillStart, onWillUpdateProps } from "@odoo/owl";
import { Layout } from "@web/search/layout";

export class LogController extends Component {
  setup() {
    this.orm = useService("orm");
    this.state = useState({ data: [] });
    this.keepLast = new KeepLast();
    onWillStart(async () => {
      const { records } = await this.loadLogs(this.props.domain);
      this.state.data = records;
    });

    onWillUpdateProps(async (nextProps) => {
      if (
        JSON.stringify(nextProps.domain) !== JSON.stringify(this.props.domain)
      ) {
        const { records } = await this.loadLogs(nextProps.domain);
        this.state.data = records;
      }
    });
  }

  loadLogs(domain) {
    return this.keepLast.add(
      this.orm.webSearchRead(this.props.resModel, domain, [
        this.props.archInfo.letterId,
      ])
    );
  }
}

LogController.template = "log_view.LogView";
LogController.components = { Layout };
