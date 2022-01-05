function drawLayer02Label(canvasObj,text,textBeginX,lineEndX){
	var colorValue = '#04918B';

	var ctx = canvasObj.getContext("2d");

	ctx.beginPath();
	ctx.arc(35,55,2,0,2*Math.PI);
	ctx.closePath();
	ctx.fillStyle = colorValue;
	ctx.fill();

	ctx.moveTo(35,55);
	ctx.lineTo(60,80);
	ctx.lineTo(lineEndX,80);
	ctx.lineWidth = 1;
	ctx.strokeStyle = colorValue;
	ctx.stroke();

	ctx.font='12px Georgia';
	ctx.fillStyle = colorValue;
	ctx.fillText(text,textBeginX,92);
}

//接入机型占比

var COLOR = {
	MACHINE:{
		TYPE_A:'#0175EE',
		TYPE_B:'#D89446',
		TYPE_C:'#373693',
		TYPE_D:'#25AE4F',
		TYPE_E:'#06B5C6',
		TYPE_F:'#009E9A',
		TYPE_G:'#AC266F'
	}
};

function renderLegend(){
	drawLegend(COLOR.MACHINE.TYPE_A,25,'上海……');
	drawLegend(COLOR.MACHINE.TYPE_B,50,'东莞……');
	drawLegend(COLOR.MACHINE.TYPE_C,75,'深圳……');
	drawLegend(COLOR.MACHINE.TYPE_D,100,'厦门……');
	drawLegend(COLOR.MACHINE.TYPE_E,125,'杭州……');
	drawLegend(COLOR.MACHINE.TYPE_F,150,'重庆……');
	drawLegend(COLOR.MACHINE.TYPE_G,175,'北京……');
}

function drawLegend(pointColor,pointY,text){
	var ctx = $("#layer03_left_01 canvas").get(0).getContext("2d");
	ctx.beginPath();
	ctx.arc(20,pointY,6,0,2*Math.PI);
	ctx.fillStyle = pointColor;
	ctx.fill();
	ctx.font='20px';
	ctx.fillStyle = '#FEFFFE';
	ctx.fillText(text,40,pointY+3);
}


//存储
function renderLayer03Right(){
	drawLayer03Right($("#layer03_right_chart01 canvas").get(0),"#027825",0.66);
	drawLayer03Right($("#layer03_right_chart02 canvas").get(0),"#006DD6",0.52);
	drawLayer03Right($("#layer03_right_chart03 canvas").get(0),"#238681",0.34);
}

function drawLayer03Right(canvasObj,colorValue,rate){
	var ctx = canvasObj.getContext("2d");

	var circle = {
        x : 65,    //圆心的x轴坐标值
        y : 80,    //圆心的y轴坐标值
        r : 60      //圆的半径
    };

	ctx.beginPath();
	ctx.arc(circle.x,circle.y,circle.r,0,Math.PI*2)
	ctx.lineWidth = 10;
	ctx.strokeStyle = '#052639';
	ctx.stroke();
	ctx.closePath();

	ctx.beginPath();
	ctx.arc(circle.x,circle.y,circle.r,1.5*Math.PI,(1.5+rate*2)*Math.PI)
	ctx.lineWidth = 10;
	ctx.lineCap = 'round';
	ctx.strokeStyle = colorValue;
	ctx.stroke();
	ctx.closePath();

	ctx.fillStyle = 'white';
	ctx.font = '20px Calibri';
	ctx.fillText(rate*100+'%',circle.x-15,circle.y+10);

}


function renderChartBar01(){
	var myChart = echarts.init(document.getElementById("layer03_left_02"));
		myChart.setOption(
					 {
						title : {
							text: '',
							subtext: '',
							x:'center'
						},
						tooltip : {
							trigger: 'item',
							formatter: "{b} : {c} ({d}%)"
						},
						legend: {
							show:false,
							x : 'center',
							y : 'bottom',
							data:["上海","东莞","中山","乌鲁木齐","佛山","兰州","北京","南京","南宁","南昌","厦门",
								"合肥","呼和浩特","哈尔滨","大连","天津","宁波","常州","广州","惠州","成都","拉萨",
								"无锡","昆山","昆明","杭州","武汉","沈阳","济南","海口","深圳","珠海","石家庄",
								"福州","苏州","西宁","西安","贵州","贵阳","郑州","重庆","银川","长春","长沙","青岛"]
						},
						toolbox: {
						},
						label:{
							normal:{
								show: true, 
								formatter: "{b} \n{d}%"
							} 
						},
						calculable : true,
						color:[COLOR.MACHINE.TYPE_A,COLOR.MACHINE.TYPE_B,COLOR.MACHINE.TYPE_C,COLOR.MACHINE.TYPE_D,COLOR.MACHINE.TYPE_E,COLOR.MACHINE.TYPE_F,COLOR.MACHINE.TYPE_G],
						series : [
							{
								name:'',
								type:'pie',
								radius : [40, 80],
								center : ['50%', '50%'],
								//roseType : 'area'
								data:[
									{value:18898.42, name:"上海"},
									{value:13861.85, name:"东莞"},
									{value:11087.98, name:"中山"},
									{value:9697.91, name:"乌鲁木齐"},
									{value:13706.56, name:"佛山"},
									{value:11111.11, name:"兰州"},
									{value:19784.11, name:"北京"},
									{value:15113.79, name:"南京"},
									{value:10091.19, name:"南宁"},
									{value:9969.65, name:"南昌"},
									{value:12765.58, name:"厦门"},
									{value:12745.19, name:"合肥"},
									{value:9273.51, name:"呼和浩特"},
									{value:9191.00, name:"哈尔滨"},
									{value:12010.48, name:"大连"},
									{value:12268.74, name:"天津"},
									{value:13116.94, name:"宁波"},
									{value:12229.12, name:"常州"},
									{value:14955.79, name:"广州"},
									{value:12679.32, name:"惠州"},
									{value:13731.30, name:"成都"},
									{value:8361.11, name:"拉萨"},
									{value:13296.08, name:"无锡"},
									{value:12933.41, name:"昆山"},
									{value:9560.56, name:"昆明"},
									{value:16979.08, name:"杭州"},
									{value:13270.19, name:"武汉"},
									{value:10181.43, name:"沈阳"},
									{value:10763.86, name:"济南"},
									{value:9951.29, name:"海口"},
									{value:18760.28, name:"深圳"},
									{value:14017.53, name:"珠海"},
									{value:9858.42, name:"石家庄"},
									{value:12108.40, name:"福州"},
									{value:14697.16, name:"苏州"},
									{value:9184.78, name:"西宁"},
									{value:13116.66, name:"西安"},
									{value:7666.67, name:"贵州"},
									{value:9727.59, name:"贵阳"},
									{value:10503.26, name:"郑州"},
									{value:12073.88, name:"重庆"},
									{value:9035.08, name:"银川"},
									{value:9871.37, name:"长春"},
									{value:12682.36, name:"长沙"},
									{value:10807.25, name:"青岛"}
								]
							}
						]
					}
		);
}


function renderLayer04Left(){
	var myChart = echarts.init(document.getElementById("layer04_left_chart"));
	myChart.setOption(
		{
			title: {
				text: ''
			},
			tooltip : {
				trigger: 'axis'
			},
			legend: {
				data:[]
			},
			grid: {
				left: '3%',
				right: '4%',
				bottom: '5%',
				top:'4%',
				containLabel: true
			},
			xAxis :
			{
				type : 'category',
				boundaryGap : false,
				data:["上海","东莞","中山","乌鲁木齐","佛山","兰州","北京","南京","南宁","南昌","厦门",
					"合肥","呼和浩特","哈尔滨","大连","天津","宁波","常州","广州","惠州","成都","拉萨",
					"无锡","昆山","昆明","杭州","武汉","沈阳","济南","海口","深圳","珠海","石家庄",
					"福州","苏州","西宁","西安","贵州","贵阳","郑州","重庆","银川","长春","长沙","青岛"],
				axisLabel:{
					textStyle:{
						color:"white", //刻度颜色
						fontSize:8  //刻度大小
					},
					rotate:45,
					interval:0
				},
				axisTick:{show:false},
				axisLine:{
					show:true,
					lineStyle:{
						color: '#0B3148',
						width: 1,
						type: 'solid'
					}
				}
			},
			yAxis : 
			{
				type : 'value',
				axisTick:{show:false},
				axisLabel:{
					textStyle:{
						color:"white", //刻度颜色
						fontSize:8  //刻度大小
						}
				},
				axisLine:{
					show:true,
					lineStyle:{
						color: '#0B3148',
						width: 1,
						type: 'solid'
					}
				},
				splitLine:{
					show:false
				}
			},
			tooltip:{
				formatter:'{c}',
				backgroundColor:'#FE8501'
			},
			series : [
				{
					name:'',
					type:'line',
					smooth:true,
					areaStyle:{
						normal:{
							color:new echarts.graphic.LinearGradient(0, 0, 0, 1, [{offset: 0, color: '#026B6F'}, {offset: 1, color: '#012138' }], false),
							opacity:0.2
						}
					},
					itemStyle : {  
                            normal : {  
                                  color:'#009991'
                            },
							lineStyle:{
								normal:{
								color:'#009895',
								opacity:1
							}
						}
                    },
					symbol:'none',
					data:[18898.41612,13861.84857,11087.98283,9697.916667,13706.55957,11111.11111,19784.10573,
						15113.78545,10091.1859,9969.650206,12765.5754,12745.1869,9273.504274,9191.006601,
						12010.47764,12268.73898,13116.93735, 12229.12492,14955.79118,12697.32143,13731.30335,
						8361.111111,13296.07843,12933.40895,9560.557053,16979.07944,13270.19231,10181.43045,
						10763.86431,9951.298701,18760.28345,14017.53181,9858.641975,12108.39599,14697.15865,
						9184.782609,13116.66146,7666.666667,9727.598566,10503.25815,12073.87742,9035.087719,
						9871.374765,12682.36297,10807.25066]
				}
			]
		}
	
	);
}
