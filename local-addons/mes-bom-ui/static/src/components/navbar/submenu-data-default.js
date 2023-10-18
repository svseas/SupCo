/**@odoo-module */
const subDefault =
{
    "index": 1,
    "label": "Giấy Giới Thiệu",
    "nested": [
        {
            "label": "Giấy Giới Thiệu",
            "actionName": "supco.action_supreme_court_letters",
            "args": {},
            "level": [
                {
                    "levelName": "Công tác báo chí",
                    "levelAction": ""
                },
                {
                    "levelName": "Giấy Giới Thiệu",
                    "levelAction": ""
                },
                {
                    "levelName": "Giấy Giới Thiệu",
                    "levelAction": "supco.action_supreme_court_letters"
                }
            ]
        },
        {
            "label": "Nhân sự báo chí",
            "actionName": "supco.action_supreme_court_employee",
            "args": {},
            "level": [
                {
                    "levelName": "Công tác báo chí",
                    "levelAction": ""
                },
                {
                    "levelName": "Giấy Giới Thiệu",
                    "levelAction": ""
                },
                {
                    "levelName": "Nhân sự báo chí",
                    "levelAction": "supco.action_supreme_court_employee"
                }
            ]
        },
        {
            "label": "Phòng ban",
            "actionName": "supco.action_supreme_court_department",
            "args": {},
            "level": [
                {
                    "levelName": "Công tác báo chí",
                    "levelAction": ""
                },
                {
                    "levelName": "Giấy Giới Thiệu",
                    "levelAction": ""
                },
                {
                    "levelName": "Phòng ban",
                    "levelAction": "supco.action_supreme_court_department"
                }
            ]
        }
    ]
};

export { subDefault };