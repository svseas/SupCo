/** @odoo-module */

import { registry } from "@web/core/registry";
import { LogController } from "./log_controller";
import { LogArchParser } from "./log_arch_parser";
import { LogRenderer } from "./log_renderer";
import { LogModel } from "./log_model";

export const logView = {
  type: "log",
  display_name: "Log",
  icon: "fa fa-picture-o",
  multiRecord: true,
  Controller: LogController,
  Model: LogModel,
  Renderer: LogRenderer,
  ArchParser: LogArchParser,

  props(genericProps, view) {
    const { ArchParser } = view;
    const { arch } = genericProps;
    const archInfo = new ArchParser().parse(arch);

    return {
      ...genericProps,
      Model: view.Model,
      Renderer: view.Renderer,
      archInfo,
    };
  },
};

registry.category("views").add("log", logView);
