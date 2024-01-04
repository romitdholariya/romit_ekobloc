// frappe.pages['summary-dashboard'].on_page_load = function(wrapper) {
// new MyPage(wrapper);	
// }

// //Page Content
// MyPage = Class.extend({
// 	init: function(wrapper){
// 		this.page = frappe.ui.make_app_page({
// 			parent: wrapper,
// 			title: 'Summary Dashboard',
// 			single_column: true
// 	});
// 	this.make();
// 	},
// 	//make function
// 	make: function(){
// 		let me = $(this); //grab class
// 		$(frappe.render_template(frappe.dashboard.body,this)).appendTo(this.page.main);
// 	}
// })
// var body = "dfsdsdds"; // body content
// frappe.dashboard={
// 	body: body
// }

// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.dashboards");
frappe.provide("frappe.dashboards.chart_sources");

frappe.pages["summary-dashboard"].on_page_load = function (wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Summary Dashboard',
		single_column: true,
	});

	frappe.dashboard = new Dashboard(wrapper);
	$(wrapper).bind("show", function () {
		frappe.dashboard.show();
	});
};

class Dashboard {
	constructor(wrapper) {
		this.wrapper = $(wrapper);
		$(`<div class="dashboard" style="overflow: visible">
			<div class="dashboard-graph"></div>
		</div>`).appendTo(this.wrapper.find(".page-content").empty());
		this.container = this.wrapper.find(".dashboard-graph");
		this.page = wrapper.page;
	}
	
	refresh() {
		frappe.run_serially([() => this.render_cards()]);
	}
	render_cards() {
		return this.get_permitted_items(
			"frappe.desk.doctype.dashboard.dashboard.get_permitted_cards"
		).then((cards) => {
			if (!cards.length) {
				return;
			}

			this.number_cards = cards.map((card) => {
				return {
					name: card.card,
				};
			});

			this.number_card_group = new frappe.widget.WidgetGroup({
				container: this.container,
				type: "number_card",
				columns: 3,
				options: {
					allow_sorting: false,
					allow_create: false,
					allow_delete: false,
					allow_hiding: false,
					allow_edit: false,
				},
				widgets: this.number_cards,
			});
		});
	}

}

