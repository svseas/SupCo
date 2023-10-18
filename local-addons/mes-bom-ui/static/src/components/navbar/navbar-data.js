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
          nested: [
            {
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
                  levelAction: "",
                },
                {
                  levelName: "Giấy Giới Thiệu",
                  levelAction: "supco.action_supreme_court_letters",
                },
              ],
            },
            {
              label: "Nhân sự báo chí",
              actionName: "supco.action_supreme_court_employee",
              args: {},
              level: [
                {
                  levelName: "Công tác báo chí",
                  levelAction: "",
                },
                {
                  levelName: "Giấy Giới Thiệu",
                  levelAction: "",
                },
                {
                  levelName: "Nhân sự báo chí",
                  levelAction: "supco.action_supreme_court_employee",
                },
              ],
            },
            {
              label: "Phòng ban",
              actionName: "supco.action_supreme_court_department",
              args: {},
              level: [
                {
                  levelName: "Công tác báo chí",
                  levelAction: "",
                },
                {
                  levelName: "Giấy Giới Thiệu",
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
          index: 2,
          label: "Công tác nghiệp vụ",
          nested: [
            {
              label: "Tổ điều tra",
              level: [
                {
                  levelName: "Công tác báo chí",
                  levelAction: "",
                },
                {
                  levelName: "Công tác nghiệp vụ",
                  levelAction: "",
                },
                {
                  levelName: "Tổ điều tra",
                  levelAction: "",
                },
              ],
            },
            {
              label: "Tổ chuyên môn",
              level: [
                {
                  levelName: "Công tác báo chí",
                  levelAction: "",
                },
                {
                  levelName: "Công tác nghiệp vụ",
                  levelAction: "",
                },
                {
                  levelName: "Tổ chuyên môn",
                  levelAction: "",
                },
              ],
            },
            {
              label: "Tổ pháp luật",
              level: [
                {
                  levelName: "Công tác báo chí",
                  levelAction: "",
                },
                {
                  levelName: "Công tác nghiệp vụ",
                  levelAction: "",
                },
                {
                  levelName: "Tổ pháp luật",
                  levelAction: "",
                },
              ],
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
      label: ["Nghiệp vụ truyền hình"],
      icon: "icon-layers",
      nested: [],
    },
    {
      index: 3,
      label: ["Công tác Đoàn"],
      icon: "icon-check-square",
      nested: [],
    },
    {
      index: 4,
      label: ["Ngoại giao"],
      icon: "icon-zap",
      nested: [],
    },
  ],
};
