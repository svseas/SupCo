/** @odoo-module */

import { registry } from "@web/core/registry";
import { LogController } from "./log_controller";
import { LogArchParser } from "./log_arch_parser";

export const logView = {
  type: "log",
  display_name: "Log",
  icon: "fa fa-picture-o",
  multiRecord: true,
  Controller: LogController,
  ArchParser: LogArchParser,

  props(genericProps, view) {
    const { ArchParser } = view;
    const { arch } = genericProps;
    const archInfo = new ArchParser().parse(arch);

    return {
      ...genericProps,
      archInfo,
    };
  },
};

registry.category("views").add("log", logView);
