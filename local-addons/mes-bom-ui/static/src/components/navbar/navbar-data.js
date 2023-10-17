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
              level: ["Công tác báo chí", "Giấy Giới Thiệu"],
            },
            {
              label: "Nhân sự báo chí",
              actionName: "supco.action_supreme_court_employee",
              level: ["Công tác báo chí", "Giấy Giới Thiệu"],
            },
            {
              label: "Phòng ban",
              actionName: "supco.action_supreme_court_department",
              level: ["Công tác báo chí", "Giấy Giới Thiệu"],
            },
          ],
        },
        {
          index: 2,
          label: "Công tác nghiệp vụ",
          nested: [
            {
              label: " Tổ điều tra",
              level: ["Công tác báo chí", "Công tác nghiệp vụ"],
            },
            {
              label: "Tổ chuyên môn",
              level: ["Công tác báo chí", "Công tác nghiệp vụ"],
            },
            {
              label: " Tổ pháp luật ",
              level: ["Công tác báo chí", "Công tác nghiệp vụ"],
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
      label: ["Quản lý sản xuất"],
      icon: "icon-file-text",
      nested: [],
    },
    {
      index: 4,
      label: ["Công tác Đoàn"],
      icon: "icon-check-square",
      nested: [],
    },
    {
      index: 5,
      label: ["Ngoại giao"],
      icon: "icon-zap",
      nested: [],
    },
    {
      index: 6,
      label: ["Quản lý vận hành thiết bị"],
      icon: "icon-sliders",
      nested: [],
    },
  ],
};
