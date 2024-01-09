/** @odoo-module */

import { BomGetData } from "../mes-get-data/mes-get-data";
import { OrmExample } from "../orm-example/orm-example";
import { ContentContainer } from "../content-container/content-container";
import { MainContent } from "../main-content/main-content";

export const navData = {
  tabSystem: ["NEWS", "HR", "INV"],
  components: [BomGetData, OrmExample, ContentContainer, MainContent],
  navItems: [
    {
      index: 1,
      label: ["Công tác báo chí"],
      icon: "icon-layout",
      nested: [
        {
          index: 1,
          label: "Giấy Giới Thiệu",
          actionName: "supco.action_supreme_court_letters",
          args: {},
          level: [
            {
              levelName: "Công tác báo chí",
              levelAction: "",
            },
            {
              levelName: "Giấy Giới Thiệu",
              levelAction: "supco.action_supreme_court_letters",
            },
          ],
        },
        {
          index: 2,
          label: "Công tác nghiệp vụ",
          actionName: "",
          args: {},
          level: [
            {
              levelName: "Công tác báo chí",
              levelAction: "",
            },
            {
              levelName: "Công tác nghiệp vụ",
              levelAction: "",
            },
          ],
        },
        {
          index: 3,
          label: "Thi đua đổi mới",
          nested: [],
        },
        {
          index: 4,
          label: "Phong trào chuyên cần",
          nested: [],
        },
        {
          index: 5,
          label: "Ban cán sự",
          nested: [],
        },
      ],
    },
    {
      index: 2,
      label: ["Nhân sự"],
      icon: "icon-zap",
      nested: [
        {
          index: 1,
          label: "Nhân sự báo chí",
          actionName: "supco.action_supreme_court_employee",
          args: {},
          level: [
            {
              levelName: "Nhân sự",
              levelAction: "",
            },
            {
              levelName: "Nhân sự báo chí",
              levelAction: "supco.action_supreme_court_employee",
            },
          ],
        },
        {
          index: 2,
          label: "Phòng ban",
          actionName: "supco.action_supreme_court_department",
          args: {},
          level: [
            {
              levelName: "Nhân sự",
              levelAction: "",
            },
            {
              levelName: "Phòng ban",
              levelAction: "supco.action_supreme_court_department",
            },
          ],
        },
      ],
    },
    {
      index: 3,
      label: ["Nghiệp vụ truyền hình"],
      icon: "icon-layers",
      nested: [],
    },
    {
      index: 4,
      label: ["Công tác Đoàn"],
      icon: "icon-check-square",
      nested: [],
    },
  ],
};
