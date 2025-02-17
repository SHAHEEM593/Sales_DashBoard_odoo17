/**@odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from  "@odoo/owl";
import { onWillStart,onMounted,useRef } from "@odoo/owl";
import { loadJS } from "@web/core/assets";

const actionRegistry = registry.category("actions");

class AdvancedDashboard extends Component {
	setup() {
		super.setup()
		this.orm = useService('orm')
		this.revenue = useRef("revenue")
		this.sale_count = useRef("sale_count")
		this.invoice_count = useRef("invoice_count")
		this.day = useRef("day")
		        this.actionService = useService("action");

		onWillStart(async () => {
			await loadJS(["/web/static/lib/Chart/Chart.js"]);
			await this._fetch_data();
		});
		onMounted(() => {
		const revenue = this.revenue.el
		var sale_count = this.sale_count.el
		var invoice_count = this.invoice_count.el
		var day = this.day.val
        });
	}
	_fetch_data() {
		var self = this;
		console.log(self)
		this.orm.call("sales.dashboard", "get_tiles_data", [], {}).then(function(result) {
			revenue.append(result.currency + " "+result.total_revenue  );
			sale_count.append(result.total_sale_count);
			invoice_count.append(result.invoice_status);
			self.chart1 = new Chart("chart1", {
				type: "bar",
				data: {
					labels: result.team,
					datasets: [{
						backgroundColor: "MediumBlue",
						data: result.total_sale,
					}]
				},
				options: {
					plugins: {
						legend: {
							display: false,

						}
					}
				}
			});
			self.chart2 = new Chart("chart2", {
				type: "pie",
				data: {
					labels: result.sale_person,
					datasets: [{
						data: result.sale_count
					}]
				},
				options: {}
			});
			self.chart3 = new Chart("chart3", {
				type: "pie",
				data: {
					labels: result.customer,
					datasets: [{
						data: result.customer_count,
						pointBackgroundColor: "black",
					}]
				},
				option: {}
			});
			self.chart4 = new Chart("chart4", {
				type: "bar",
				data: {
					labels: result.lowest_selling_product,

					datasets: [{
						backgroundColor: "MediumBlue",
						data: result.lowest_count
					}]
				},
				options: {
					plugins: {
						legend: {
							display: false,

						}
					}
				}
			});
			self.chart5 = new Chart("chart5", {
				type: "line",
				data: {
					labels: result.highest_selling_product,

					datasets: [{
						backgroundColor: "MediumBlue",
						data: result.highest_count
					}]
				},
				options: {
					plugins: {
						legend: {
							display: false,

						}
					}
				}
			});
			self.chart6 = new Chart("chart6", {
				type: "pie",
				data: {
					labels: ['Sale', 'Canceled'],

					datasets: [{
						data: result.status
					}]
				},
				options: {}
			});

		});

	};
	myFunction() {
		var self = this;
		if (day == 'week') {
			self.chart1.destroy()
			this.orm.call("sales.dashboard", "get_week_data", [], {}).then(function(result) {
				self.chart1 = new Chart("chart1", {
					type: "bar",
					data: {
						labels: result.sale_team_name,
						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.sale_team_count,
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart2.destroy()
				self.chart2 = new Chart("chart2", {
					type: "pie",
					data: {
						labels: result.sales_person,

						datasets: [{
							data: result.sales_person_count
						}]
					},
					options: {}
				});
				self.chart3.destroy()
				self.chart3 = new Chart("chart3", {
					type: "pie",
					data: {
						labels: result.customer,
						datasets: [{
							data: result.customer_count,
							pointBackgroundColor: "black",
						}]
					},
					option: {}
				});
				self.chart4.destroy()
				self.chart4 = new Chart("chart4", {
					type: "bar",
					data: {
						labels: result.lowest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.lowest_count
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart5.destroy()
				self.chart5 = new Chart("chart5", {
					type: "line",
					data: {
						labels: result.highest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.highest_count
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart6.destroy()
				self.chart6 = new Chart("chart6", {
					type: "pie",
					data: {
						labels: ['Sale', 'Canceled'],

						datasets: [{
							data: result.status
						}]
					},
					options: {}
				});

			})
		} else if (day == 'year') {
			self.chart1.destroy()
			this.orm.call("sales.dashboard", "get_year_data", [], {}).then(function(result) {
				self.chart1 = new Chart("chart1", {
					type: "bar",
					data: {
						labels: result.sale_team_name,
						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.sale_team_count,
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart2.destroy()
				self.chart2 = new Chart("chart2", {
					type: "pie",
					data: {
						labels: result.sales_person,

						datasets: [{
							data: result.sales_person_count
						}]
					},
					options: {}
				});
				self.chart3.destroy()
				self.chart3 = new Chart("chart3", {
					type: "pie",
					data: {
						labels: result.customer,
						datasets: [{
							data: result.customer_count,
							pointBackgroundColor: "black",
						}]
					},
					option: {}
				});
				self.chart4.destroy()
				self.chart4 = new Chart("chart4", {
					type: "bar",
					data: {
						labels: result.lowest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.lowest_count
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart5.destroy()
				self.chart5 = new Chart("chart5", {
					type: "line",
					data: {
						labels: result.highest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.highest_count
						}]
					},
					options: {
						plugins: {
							legend: {
								display: false,

							}
						}
					}
				});
				self.chart6.destroy()
				self.chart6 = new Chart("chart6", {
					type: "pie",
					data: {
						labels: ['Sale', 'Canceled'],

						datasets: [{
							data: result.status
						}]
					},
					options: {}
				});
			})
		} else {
			this.orm.call("sales.dashboard", "get_tiles_data", [], {}).then(function(result) {
				console.log('res', result)
				self.chart1.destroy()
				self.chart1 = new Chart("chart1", {
					type: "bar",
					data: {
						labels: result.team,
						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.total_sale,
						}]
					},
					options: {}
				});
				self.chart2.destroy()
				self.chart2 = new Chart("chart2", {
					type: "pie",
					data: {
						labels: result.sale_person,

						datasets: [{
							data: result.sale_count
						}]
					},
					options: {}
				});
				self.chart3.destroy()
				self.chart3 = new Chart("chart3", {
					type: "pie",
					data: {
						labels: result.customer,
						datasets: [{
							data: result.customer_count,
							pointBackgroundColor: "black",
						}]
					},
					option: {}
				});
				self.chart4.destroy()
				self.chart4 = new Chart("chart4", {
					type: "bar",
					data: {
						labels: result.lowest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.lowest_count
						}]
					},
					options: {}
				});
				self.chart5.destroy()
				self.chart5 = new Chart("chart5", {
					type: "line",
					data: {
						labels: result.highest_selling_product,

						datasets: [{
							backgroundColor: "MediumBlue",
							data: result.highest_count
						}]
					},
					options: {}
				});
				self.chart6.destroy()

				self.chart6 = new Chart("chart6", {
					type: "pie",
					data: {
						labels: ['Sale', 'Canceled'],

						datasets: [{
							data: result.status
						}]
					},
					options: {}
				});
			});
		}
	}
	totalRevenue(){
	        return this.actionService.doAction({
            type: 'ir.actions.act_window',
            name: 'Total Revenue',
            res_model: 'sale.order',
            views: [[false, 'list']],
            view_type: 'tree',
            view_mode: 'tree',
            target: 'current',
	})
}
}

AdvancedDashboard.template = "sales_dashboard.SaleDashboard";
actionRegistry.add("advanced_dashboard", AdvancedDashboard)

