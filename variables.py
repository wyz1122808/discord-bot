token = 'MTA3NDc0NTEyMzA3OTk4NzIxMA.GiK4U1.Oj4JABhq-wAHNsum0qr-5XayinP33fe2EvALas'
#  ink: MTA4MDI2MjQ1MjMyOTA3MDY5Mw.GLnb50.pPG2rxgFqfOhhn1C0YUXAiQT_6NVwEtsD81hM8
# daisensei: MTA3NDc0NTEyMzA3OTk4NzIxMA.GiK4U1.Oj4JABhq-wAHNsum0qr-5XayinP33fe2EvALas

from enum import Enum


class GiftName(str, Enum):
    游戏机 = "游戏机",
    气噗噗的老头 = "气噗噗的老头",
    SB14K = "SB14K",
    印花集 = "印花集",
    要抱抱 = "要抱抱",
    枪响人亡 = "枪响人亡",
    生日蛋糕 = "生日蛋糕",
    水栽竹 = "水栽竹",
    美杜莎 = "美杜莎",
    波塞冬 = "波塞冬",
    半日冠名 = "半日冠名 - 女神之泪",
    一日冠名 = "一日冠名",
    三日冠 = "三日冠 - 骑士之誓",
    五日冠名 = "五日冠名 - 救赎",
    周冠名 = "周冠名 - 炙热香炉",
    半月冠 = "半月冠 - 双生暗影",
    月冠 = '月冠 - 潘多拉的秘密',
    季冠名 = "季冠名 - 自然之力",
    年冠名 = "年冠名 - 无限宝珠",
    歌手半日冠 = "歌手半日冠",
    歌手日冠名 = "歌手日冠名",
    儿童节全套玩具 = '儿童节全套玩具',
    虚拟恋人 = "虚拟恋人"


class foodName(str, Enum):
    胡辣汤 = "胡辣汤，是中国河南、陕西等地的汤类食品。 常作为早餐，其特点是麻辣鲜香，食用时常搭配油条、包子等其它早点。",
    肉夹馍 = "肉夹馍的叫法源自古汉语，是一种宾语前置，其意为“肉夹在馍中”，好吃实惠。",
    锅包肉 = "锅包肉（英文名：Fried Pork in Scoop），光绪年间始创自哈尔滨道台府府尹杜学瀛厨师郑兴文之手。 成菜后，色泽金黄，口味酸甜。 锅包肉是为适应外宾口味，把咸鲜口味的“焦烧肉条”改成了一道酸甜口味的菜肴。",
    小龙虾 = "麻辣小龙虾又名口味虾、长沙口味虾、香辣小龙虾，是湖南著名的地方小吃。 麻辣小龙虾以小龙虾为主材，配以辣椒、花椒和其他香辛料制成。成菜后，色泽红亮，口味辣并鲜香。",
    重庆火锅 = "重庆火锅，又称毛肚火锅或麻辣火锅，是中国传统饮食方式之一；以“辣、麻、咸、鲜、香、脆”为其口味，具有菜品多样、调味独特、吃法豪放等特点",
    碗仔翅 = "碗仔翅是一種香港街頭仿魚翅羹小吃[1]，其材料以粉絲為主，以澱粉將湯煮至濃稠，並加入老抽和生抽成棕色，冬菇絲和雞肉絲常被加入一起烹調，使湯羹的口感更為充實。進食碗仔翅時，可按個人喜好加入麻油、浙醋、白胡椒粉或辣椒油調味",
    虾饺 = "虾饺是广东省广州市的一种特色小吃，属于粤菜系，该菜品始创于20世纪初广州市郊伍村五凤乡的一间家庭式小茶楼，已经有百年历史；传统的虾饺是半月形、蜘蛛肚共有十二褶的，馅料有虾，有肉，有笋，味道鲜美爽滑，美味可口。",
    杨枝甘露 = "杨枝甘露指的是一种粤式甜品，主要食材是西柚、芒果、西米、椰浆，主要烹饪工艺是煮。芒果和西柚都含有丰富的维生素，是一道营养丰富的甜品。",
    东坡肉 = "宋人东坡先生的那首《猪肉颂》：“黄州有好肉，价钱如泥土，贵者不肯吃，贫者不解煮”。",
    咖喱鱼蛋 = "咖喱鱼蛋是一道地方小吃，属于闽菜、粤菜。口感弹牙，鲜嫩，海鲜味十足。因酱料不同有甜辣、酸甜等各种口味。咖喱鱼蛋是用特种咖喱粉及各种秘制酱料，将正宗的潮汕鱼丸、台湾鱼丸或者福建鱼丸在锅中煮，待鱼丸煮熟后盛出淋上甜辣酱或蕃茄酱等，可食用。",
    白切鸡 = "白切鸡始于清代，因烹制时不加调味白煮而成以保持原味，肉质刚熟不烂且食用时随吃随斩，故又称“白斩鸡”。 白切鸡色泽洁白油黄，皮爽肉滑骨香，原汁原味，清淡鲜美。",
    茅台 = "茅台酒是一款酱香型白酒，采用高温制曲，二次投料，堆积发酵的生产工艺，一般一年为一个生产周期。 取酒后经过勾兑、陈贮而成。 其酒味呈酱香、窖底香、醇甜香而具独特风格。 酒体完美，香气幽雅，酒味丰满、醇厚。",
    红烧肉 = "一道著名的大众菜肴，各大菜系都有自己特色的红烧肉。其以五花肉为制作主料，也可用猪后腿代替，最好选用肥瘦相间的三层肉来做，锅具以砂锅为主，做出来的肉肥瘦相间，肥而不腻，香甜松软，营养丰富，入口即化。",
    小笼包 = "小笼包，是一种诞生于中国江南地区的著名点心，吴语区以外又称小笼包，多处地方亦盛行，例如广东、香港、台湾，以“体小、馅大、汁多、味鲜、皮薄、形美”而著称。 汤包源于北宋京城开封的灌汤包，现代形式的小笼包起源于江南，后又在各地得到发展和演变，形成不同的口味。",
    热干面 = "热干面色泽黄而油润，味道鲜美，由于热量高，也可以当作主食，营养早餐，补充人体所需的能量。是武汉最出名的小吃之一。",
    羊肉泡馍 = "羊肉泡馍，亦称羊肉泡，古称“羊羹”，关中汉族风味饭食，源自西周。它烹制精细，料重味醇，肉烂汤浓，肥而不腻，营养丰富，香气四溢，诱人食欲，食后回味无穷。",
    钵钵鸡 = "钵钵鸡是一种四川传统名小吃，属于川菜系。从清代流传至今已有上百年的历史。是以陶器钵盛放配以麻辣为主的佐料，加上多种调料的去骨鸡片拌和而成。有皮脆肉嫩，麻辣鲜香，甜咸适中的特色",
    糖醋排骨 = "糖醋排骨是川菜糖醋味型中具有代表性的一道大众喜爱的传统菜，因为口味香脆酸甜，颇受江浙沪人士喜爱。",
    豆腐脑 = "豆腐脑又称水豆腐，是一道著名的传统特色小吃。利用大豆蛋白制成的高营养食品，多在晨间出售，常与豆腐花、豆花混用，依据各地口味不同，北方多爱咸食，而南方则偏爱甜味，亦有地区如四川等喜爱酸辣口味。",
    饺子 = "饺子  初名馄饨，又有角子、角儿、匾食、扁食、牢丸、粉角、饺饵、水饺饵、水点心、水饺子、饺儿等多种称呼。饺子的烹饪方法多样，有煮、蒸、煎、烤等。自宋代开始，有了冬至日吃饺子的习俗，自明朝以来有了正月初一吃饺子的习俗。",
    玉米排骨汤 = "玉米排骨汤 是一道食补汤品，主要食材是玉米和排骨，主要烹饪工艺是炖。玉米可降低血液胆固醇浓度并防止其沉积于血管壁，营养丰富，促进人们对维生素和钙的吸收。",
    粉蒸肉 = "粉蒸肉 ，亦称米粉肉，发源于江西。诗人袁枚在《随园食单》中首次记载为一道江西菜品，流行于中国南方（四川、江西、湖南、安徽、湖北、浙江、福建、广东梅州等地 ），所需材料主要是米粉和肉，烹饪方式是蒸。 属赣菜系",
    大闸蟹 = "大闸蟹是中国传统的名贵、出口水产品之一。肉质细嫩，滋味鲜美，营养价值极高，所含蛋白质与海蟹相等，比鲫鱼要高；所含脂肪和碳水化合物远远高于沼虾、对虾、带鱼等；维生素A非常丰富，含铁质特别高，核黄素含量也多，属高级营养食品。",
    清蒸鱼 = "清蒸鱼是用各类鱼制作的一道家常菜，主要原材料有鱼、生姜、香蒜等，口味咸鲜，鱼肉软嫩，鲜香味美，汤清味醇，具有养血和开胃的功效，是舌尖上的美食。",
    红烧狮子头 = "红烧狮子头  ，是一道淮扬名菜。将有肥有瘦的肉配上荸荠，香菇等材料，做成丸子，然后先炸后煮",
    章鱼丸子 = "章鱼丸子是一种美食，主要材料有章鱼、海苔、高丽菜等，起源于日本，特点制作简单，口味独特，口感鲜嫩，工艺性较强，深受欢迎。",
    另一个红烧肉 = "红烧肉，一道著名的大众菜肴，各大菜系都有自己特色的红烧肉。其以五花肉为制作主料，也可用猪后腿代替，最好选用肥瘦相间的三层肉来做，锅具以砂锅为主，做出来的肉肥瘦相间，肥而不腻，香甜松软，营养丰富，入口即化。",
    油焖大虾 = "油焖大虾是山东省的一道特色名菜，属于鲁菜。该菜品的主要食材为清明前渤海湾的大对虾，使用鲁菜特有的油焖技法。其是一道历史悠久的名菜，鲜香甜咸四种味道相辅相成，回味无穷。",
    毛血旺 = "毛血旺是川菜的一道特色名菜，也是重庆江湖菜的鼻祖之一，已经列入国家标准委员会《渝菜烹饪标准体系》。毛血旺以鸭血为制作主料，烹饪技巧以煮菜为主，口味属于麻辣味。其起源于重庆，流行于西南地区，是一道著名的传统菜式，这道菜是将生血旺现烫现吃，且毛肚杂碎为主料，遂得名。",
    可乐鸡翅 = "可乐鸡翅具有味道鲜美、色泽艳丽、鸡肉嫩滑、咸甜适中的特点。一般人群均可食用，不适合感冒发热、内火偏旺、痰湿偏重的人。患有热毒疖肿、高血压、血脂偏高、胆囊炎、胆石症、糖尿病患者忌食。",
    腊八粥 = "腊八粥，又称七宝五味粥、佛粥、大家饭等，是一种由多样食材熬制而成的粥。“喝腊八粥”是腊八节的习俗，腊八粥的传统食材包括大米、小米、玉米、薏米、红枣、莲子、花生、桂圆和各种豆类",
    宫保鸡丁 = "宫保鸡丁是一道闻名中外的特色传统名菜，在鲁菜、川菜、贵州菜中都有收录，其原料、做法有差别。该菜式的起源与鲁菜中的酱爆鸡丁、贵州菜中的胡辣子鸡丁有关，后被清朝山东巡抚、四川总督丁宝桢改良发扬，形成了一道新菜式——宫保鸡丁，并流传，此道菜也被归纳为北京宫廷菜。之后宫保鸡丁也流传到国外",
    回锅肉 = "回锅肉，是四川传统菜式中家常菜肴的代表菜之一，属于川菜。其制作原料主要有猪后臀肉（二刀肉）、青椒、蒜苗等，口味独特，色泽红亮，肥而不腻。",
    北京烤鸭 = "北京烤鸭是起源于南北朝时期的宫廷名菜，用优质肉食鸭，果木炭火烤制，色泽红润，肉质肥而不腻，外脆里嫩，肉质细腻、味道醇厚1。北京烤鸭分为两大流派，即全聚德和便宜坊，它们都以色泽红艳、肉质细嫩、味道醇厚、肥而不腻的特色而著名。正宗北京烤鸭的食材和调料包括京白鸭、馒头等。吃法有三种，可以将鸭肉卷在薄饼里配以葱、黄瓜、甜面酱等，也可以直接食用鸭肉，还可以将鸭骨熬成汤",
    草莓蛋糕卷 = "草莓蛋糕卷是一道美食，主料是中筋面粉、蛋，配料是温牛奶、草莓粉，调料为白醋等，主要通过烘烤的方法制作而成。",
    肠仔包 = "肠仔包，是一种美味又可口的食物，带有葱香味的美味肠仔包，柔软咸香的口感，且不宜多食。",
    珍珠奶茶 = "珍珠奶茶，又称波霸奶茶（英语：Boba milk tea）、泡泡茶，是1980年代起源于台湾的茶类饮料，为台湾泡沫红茶、粉圆茶饮文化中的分支，其作法为将粉圆加入奶茶中，奶茶可以是由奶精或鲜乳调制；另有“珍珠红（绿）茶”、“珍珠奶绿”等衍生种类，为台湾最具代表性的手摇饮料之一，并从台湾流行至世界各地。",
    冬阴功汤 = "冬阴功汤，是泰国和老挝的一道富有特色的酸辣口味汤品。也叫作东炎汤，在泰国非常普遍。主要食材有柠檬叶、香茅、虾等。",
    蚵仔煎 = "蚵仔煎是一道聞名於臺灣的小吃，在新加坡、馬來西亞類似為蠔煎，而在福建、潮汕地區有海蠣煎。差別在於臺灣的加入地瓜粉、太白粉，新加坡、馬來西亞以蛋為主，而福建、潮汕則以麵粉摻入為主。",
    生煎馒头 = "生煎馒头是流行于上海、苏州及其他江南地区的一种传统小吃，简称为生煎；亦称生煎包，类似于锅贴和水煎包，为煎熟了的有馅馒头（包子）。 生煎馒头的馅料通常使用猪肉，也可用鸡肉作原料，在一些考究的店家研发了虾肉、蟹肉等馅料。",
    大肠包小肠 = "大肠包小肠是台湾一种小吃，发源于台湾花莲的客家人出门工作时的点心，于公元一九九零年代开始在台湾夜市流行，并在现在成为台湾普遍的美食。在许多景点常有小摊贩与客人以骰子对赌，故有句俗谚曰“黑无肠，白无肠，大肠包小肠”。大肠包小肠与美国的热狗有异曲同工之妙。",
    筒仔米糕 = "筒仔米糕是一样常见于糯米类小吃，与油饭、米糕类似，但却是在瓷瓶、竹筒或铁罐中炊煮而成，口味浓郁。 有些店家会再淋上肉燥和加上肉松、香菜、萝卜干。",
    咸酥鸡 = "咸酥鸡，或称盐酥鸡，是常见的台湾小吃之一，为台湾最常见的炸鸡块，特点是会加入九层塔一起油炸，带有特殊的香气。 盐酥鸡原本是鸡肉切成小块，先以酱料腌渍入味，再裹上油炸粉或调味过后的面粉浆，再油炸的料理，因后来材料的增加，现在盐酥鸡往往是一个各种炸物综合性的全称，常见的有花椰菜、杏鲍菇、鸡皮、四季豆、银丝卷等。",
    鲜肉馄饨 = "鲜肉馄饨 ，别名鲜肉抄手，是一道以肥瘦猪肉，小麦面粉，荠菜，干紫菜作为主要食材，料酒、盐、胡椒粉、香油作为调料制作而成的食品。",
    葱油拌面 = "葱油拌面是一道以面条、食用油、黄瓜丝、葱、姜、盐、鸡精、酱油、白糖、料酒、桂皮、大料作为食材制作而成的家常面食。 通常是将煮熟的面条放上葱油一起拌着吃。 葱油拌面是上海招牌美食，面条有韧劲又滑爽，品种包括开洋葱油面、葱油肉丝面、葱油三虾面。",
    腌笃鲜 = "腌肚鲜是徽菜、苏帮菜、上海菜、杭帮菜的一种春季时令菜式，用冬笋、咸肉、豆腐皮结和鲜猪肉，置于文火上慢炖。此菜适合家庭制作，讲究原汁原味，无需添加盐、味精等任何调料。",
    条头糕 = "条头糕是江沪地区传统特色糕点，是糯米粉糅合细沙做成长条状。 撒上桂花末更好吃。 作为江南点心一大特色，清代苏州文士顾禄所著的《清嘉录》中提到了条头糕。 二十世纪三十年代，夏衍在《懒寻旧梦录》里也写到：“那时候学校里是可以向校役订点心的，如条头糕、麻酥糖之类”。",
    粢饭糕 = "粢饭糕（拼音：zī fàn gāo）是一种流行于江南一带的传统小吃，属油炸类糕点，因其做法也可称为油氽粢饭糕，南方其他地区称之为炸糍粑。粢饭糕外层呈金黄色，内层为雪白的软糯糍饭，咬起来喷香松脆。",
    锅贴 = "锅贴，中国著名传统小吃，属于煎烙煮馅类食品。制作精巧，味道可口。根据季节配以不同鲜蔬菜。锅贴的形状各地不同，一般是细长饺子形状，但天津锅贴类似褡裢火烧。",
    八宝鸭 = "八宝鸭是苏州、上海一带的一道特色传统名菜，属于沪菜、苏菜，八宝鸭是用带骨鸭开背，填入配料，扣在大碗里，封以玻璃纸蒸熟，鸭形丰腴饱满，原汁突出，出笼时再浇上用蒸鸭原卤调制的虾仁和青豆，满堂皆香。",
    熏鱼 = "熏鱼主要产自江苏、浙江、上海一带，作为当地过年必备的食品，温中补虚，有利湿、暖胃和平肝、祛风等功效。明代《宋氏养生部》中详细记载：“治鱼为大轩，微腌，焚砻谷糠，熏熟燥。治鱼微腌，油煎之，日暴之，始烟熏之。”",
    红烧猪蹄 = "红烧猪蹄  红烧猪蹄是一道传统的名菜，也是一道比较常见的家常菜，以猪蹄为主要食材，这道菜味道可口，营养价值丰富，具有美容养颜、抗衰老、促进生长、改善冠心病等功效。",
    盐酥鸡 = "鹹酥雞主要成分是雞肉，在台灣各地都有號稱是發源的老店，表示這種以雞肉塊沾粉油炸的小吃其實是多方源起的概念，有些人會稱鹹酥雞發明者是1975年臺北市西門町的「台灣第一家塩酥雞」，但事實上那只是一間調味粉批發商的名稱而已，以時間點來看更早創業的鹽酥雞攤位大有人在。"


foods = {

    " 胡辣汤 ": "胡辣汤，是中国河南、陕西等地的汤类食品。 常作为早餐，其特点是麻辣鲜香，食用时常搭配油条、包子等其它早点。",
    " 肉夹馍 ": "肉夹馍的叫法源自古汉语，是一种宾语前置，其意为“肉夹在馍中”，好吃实惠。",
    " 锅包肉 ": "锅包肉（英文名：Fried Pork in Scoop），光绪年间始创自哈尔滨道台府府尹杜学瀛厨师郑兴文之手。 成菜后，色泽金黄，口味酸甜。 锅包肉是为适应外宾口味，把咸鲜口味的“焦烧肉条”改成了一道酸甜口味的菜肴。",
    " 小龙虾 ": "麻辣小龙虾又名口味虾、长沙口味虾、香辣小龙虾，是湖南著名的地方小吃。 麻辣小龙虾以小龙虾为主材，配以辣椒、花椒和其他香辛料制成。成菜后，色泽红亮，口味辣并鲜香。",
    "重庆火锅": "重庆火锅，又称毛肚火锅或麻辣火锅，是中国传统饮食方式之一；以“辣、麻、咸、鲜、香、脆”为其口味，具有菜品多样、调味独特、吃法豪放等特点",
    " 碗仔翅 ": "碗仔翅是一種香港街頭仿魚翅羹小吃[1]，其材料以粉絲為主，以澱粉將湯煮至濃稠，並加入老抽和生抽成棕色，冬菇絲和雞肉絲常被加入一起烹調，使湯羹的口感更為充實。進食碗仔翅時，可按個人喜好加入麻油、浙醋、白胡椒粉或辣椒油調味",
    "  虾饺  ": "虾饺是广东省广州市的一种特色小吃，属于粤菜系，该菜品始创于20世纪初广州市郊伍村五凤乡的一间家庭式小茶楼，已经有百年历史；传统的虾饺是半月形、蜘蛛肚共有十二褶的，馅料有虾，有肉，有笋，味道鲜美爽滑，美味可口。",
    "杨枝甘露": "杨枝甘露指的是一种粤式甜品，主要食材是西柚、芒果、西米、椰浆，主要烹饪工艺是煮。芒果和西柚都含有丰富的维生素，是一道营养丰富的甜品。",
    " 东坡肉 ": "宋人东坡先生的那首《猪肉颂》：“黄州有好肉，价钱如泥土，贵者不肯吃，贫者不解煮”。",
    "咖喱鱼蛋": "咖喱鱼蛋是一道地方小吃，属于闽菜、粤菜。口感弹牙，鲜嫩，海鲜味十足。因酱料不同有甜辣、酸甜等各种口味。咖喱鱼蛋是用特种咖喱粉及各种秘制酱料，将正宗的潮汕鱼丸、台湾鱼丸或者福建鱼丸在锅中煮，待鱼丸煮熟后盛出淋上甜辣酱或蕃茄酱等，可食用。",
    " 白切鸡 ": "白切鸡始于清代，因烹制时不加调味白煮而成以保持原味，肉质刚熟不烂且食用时随吃随斩，故又称“白斩鸡”。 白切鸡色泽洁白油黄，皮爽肉滑骨香，原汁原味，清淡鲜美。",
    "茅台": "茅台酒是一款酱香型白酒，采用高温制曲，二次投料，堆积发酵的生产工艺，一般一年为一个生产周期。 取酒后经过勾兑、陈贮而成。 其酒味呈酱香、窖底香、醇甜香而具独特风格。 酒体完美，香气幽雅，酒味丰满、醇厚。",
    " 红烧肉 ": "一道著名的大众菜肴，各大菜系都有自己特色的红烧肉。其以五花肉为制作主料，也可用猪后腿代替，最好选用肥瘦相间的三层肉来做，锅具以砂锅为主，做出来的肉肥瘦相间，肥而不腻，香甜松软，营养丰富，入口即化。",
    " 小笼包 ": "小笼包，是一种诞生于中国江南地区的著名点心，吴语区以外又称小笼包，多处地方亦盛行，例如广东、香港、台湾，以“体小、馅大、汁多、味鲜、皮薄、形美”而著称。 汤包源于北宋京城开封的灌汤包，现代形式的小笼包起源于江南，后又在各地得到发展和演变，形成不同的口味。",
    " 热干面 ": "热干面色泽黄而油润，味道鲜美，由于热量高，也可以当作主食，营养早餐，补充人体所需的能量。是武汉最出名的小吃之一。",
    "羊肉泡馍": "羊肉泡馍，亦称羊肉泡，古称“羊羹”，关中汉族风味饭食，源自西周。它烹制精细，料重味醇，肉烂汤浓，肥而不腻，营养丰富，香气四溢，诱人食欲，食后回味无穷。",
    " 钵钵鸡 ": "钵钵鸡是一种四川传统名小吃，属于川菜系。从清代流传至今已有上百年的历史。是以陶器钵盛放配以麻辣为主的佐料，加上多种调料的去骨鸡片拌和而成。有皮脆肉嫩，麻辣鲜香，甜咸适中的特色",
    "糖醋排骨": "糖醋排骨是川菜糖醋味型中具有代表性的一道大众喜爱的传统菜，因为口味香脆酸甜，颇受江浙沪人士喜爱。",
    " 豆腐脑 ": "豆腐脑又称水豆腐，是一道著名的传统特色小吃。利用大豆蛋白制成的高营养食品，多在晨间出售，常与豆腐花、豆花混用，依据各地口味不同，北方多爱咸食，而南方则偏爱甜味，亦有地区如四川等喜爱酸辣口味。",
    "  饺子  ": "饺子  初名馄饨，又有角子、角儿、匾食、扁食、牢丸、粉角、饺饵、水饺饵、水点心、水饺子、饺儿等多种称呼。饺子的烹饪方法多样，有煮、蒸、煎、烤等。自宋代开始，有了冬至日吃饺子的习俗，自明朝以来有了正月初一吃饺子的习俗。",
    "玉米排骨汤": "玉米排骨汤 是一道食补汤品，主要食材是玉米和排骨，主要烹饪工艺是炖。玉米可降低血液胆固醇浓度并防止其沉积于血管壁，营养丰富，促进人们对维生素和钙的吸收。",
    " 粉蒸肉 ": "粉蒸肉 ，亦称米粉肉，发源于江西。诗人袁枚在《随园食单》中首次记载为一道江西菜品，流行于中国南方（四川、江西、湖南、安徽、湖北、浙江、福建、广东梅州等地 ），所需材料主要是米粉和肉，烹饪方式是蒸。 属赣菜系",
    " 大闸蟹 ": "大闸蟹是中国传统的名贵、出口水产品之一。肉质细嫩，滋味鲜美，营养价值极高，所含蛋白质与海蟹相等，比鲫鱼要高；所含脂肪和碳水化合物远远高于沼虾、对虾、带鱼等；维生素A非常丰富，含铁质特别高，核黄素含量也多，属高级营养食品。",
    " 清蒸鱼 ": "清蒸鱼是用各类鱼制作的一道家常菜，主要原材料有鱼、生姜、香蒜等，口味咸鲜，鱼肉软嫩，鲜香味美，汤清味醇，具有养血和开胃的功效，是舌尖上的美食。",
    "红烧狮子头": "红烧狮子头  ，是一道淮扬名菜。将有肥有瘦的肉配上荸荠，香菇等材料，做成丸子，然后先炸后煮",
    "章鱼丸子": "章鱼丸子是一种美食，主要材料有章鱼、海苔、高丽菜等，起源于日本，特点制作简单，口味独特，口感鲜嫩，工艺性较强，深受欢迎。",
    "    肉燕    ": "肉燕别称扁肉燕。但是肉燕皮是由猪肉加番薯粉手工打制而成。是福州一大特色小吃，肉燕有别于福建其他地区的扁肉（扁食），两者口感是完全不一样的。燕皮薄如白纸，其色似玉，口感软嫩，韧而有劲。",
    "油焖大虾": "油焖大虾是山东省的一道特色名菜，属于鲁菜。该菜品的主要食材为清明前渤海湾的大对虾，使用鲁菜特有的油焖技法。其是一道历史悠久的名菜，鲜香甜咸四种味道相辅相成，回味无穷。",
    " 毛血旺 ": "毛血旺是川菜的一道特色名菜，也是重庆江湖菜的鼻祖之一，已经列入国家标准委员会《渝菜烹饪标准体系》。毛血旺以鸭血为制作主料，烹饪技巧以煮菜为主，口味属于麻辣味。其起源于重庆，流行于西南地区，是一道著名的传统菜式，这道菜是将生血旺现烫现吃，且毛肚杂碎为主料，遂得名。",
    "可乐鸡翅": "可乐鸡翅具有味道鲜美、色泽艳丽、鸡肉嫩滑、咸甜适中的特点。一般人群均可食用，不适合感冒发热、内火偏旺、痰湿偏重的人。患有热毒疖肿、高血压、血脂偏高、胆囊炎、胆石症、糖尿病患者忌食。",
    " 腊八粥 ": "腊八粥，又称七宝五味粥、佛粥、大家饭等，是一种由多样食材熬制而成的粥。“喝腊八粥”是腊八节的习俗，腊八粥的传统食材包括大米、小米、玉米、薏米、红枣、莲子、花生、桂圆和各种豆类",
    "宫保鸡丁": "宫保鸡丁是一道闻名中外的特色传统名菜，在鲁菜、川菜、贵州菜中都有收录，其原料、做法有差别。该菜式的起源与鲁菜中的酱爆鸡丁、贵州菜中的胡辣子鸡丁有关，后被清朝山东巡抚、四川总督丁宝桢改良发扬，形成了一道新菜式——宫保鸡丁，并流传，此道菜也被归纳为北京宫廷菜。之后宫保鸡丁也流传到国外",
    " 回锅肉 ": "回锅肉，是四川传统菜式中家常菜肴的代表菜之一，属于川菜。其制作原料主要有猪后臀肉（二刀肉）、青椒、蒜苗等，口味独特，色泽红亮，肥而不腻。",
    "北京烤鸭": "北京烤鸭是起源于南北朝时期的宫廷名菜，用优质肉食鸭，果木炭火烤制，色泽红润，肉质肥而不腻，外脆里嫩，肉质细腻、味道醇厚1。北京烤鸭分为两大流派，即全聚德和便宜坊，它们都以色泽红艳、肉质细嫩、味道醇厚、肥而不腻的特色而著名。正宗北京烤鸭的食材和调料包括京白鸭、馒头等。吃法有三种，可以将鸭肉卷在薄饼里配以葱、黄瓜、甜面酱等，也可以直接食用鸭肉，还可以将鸭骨熬成汤",
    "草莓蛋糕卷": "草莓蛋糕卷是一道美食，主料是中筋面粉、蛋，配料是温牛奶、草莓粉，调料为白醋等，主要通过烘烤的方法制作而成。",
    " 肠仔包 ": "肠仔包，是一种美味又可口的食物，带有葱香味的美味肠仔包，柔软咸香的口感，且不宜多食。",
    "珍珠奶茶": "珍珠奶茶，又称波霸奶茶（英语：Boba milk tea）、泡泡茶，是1980年代起源于台湾的茶类饮料，为台湾泡沫红茶、粉圆茶饮文化中的分支，其作法为将粉圆加入奶茶中，奶茶可以是由奶精或鲜乳调制；另有“珍珠红（绿）茶”、“珍珠奶绿”等衍生种类，为台湾最具代表性的手摇饮料之一，并从台湾流行至世界各地。",
    "冬阴功汤": "冬阴功汤，是泰国和老挝的一道富有特色的酸辣口味汤品。也叫作东炎汤，在泰国非常普遍。主要食材有柠檬叶、香茅、虾等。",
    " 蚵仔煎 ": "蚵仔煎是一道聞名於臺灣的小吃，在新加坡、馬來西亞類似為蠔煎，而在福建、潮汕地區有海蠣煎。差別在於臺灣的加入地瓜粉、太白粉，新加坡、馬來西亞以蛋為主，而福建、潮汕則以麵粉摻入為主。",
    "生煎馒头": "生煎馒头是流行于上海、苏州及其他江南地区的一种传统小吃，简称为生煎；亦称生煎包，类似于锅贴和水煎包，为煎熟了的有馅馒头（包子）。 生煎馒头的馅料通常使用猪肉，也可用鸡肉作原料，在一些考究的店家研发了虾肉、蟹肉等馅料。",
    "大肠包小肠": "大肠包小肠是台湾一种小吃，发源于台湾花莲的客家人出门工作时的点心，于公元一九九零年代开始在台湾夜市流行，并在现在成为台湾普遍的美食。在许多景点常有小摊贩与客人以骰子对赌，故有句俗谚曰“黑无肠，白无肠，大肠包小肠”。大肠包小肠与美国的热狗有异曲同工之妙。",
    "筒仔米糕": "筒仔米糕是一样常见于糯米类小吃，与油饭、米糕类似，但却是在瓷瓶、竹筒或铁罐中炊煮而成，口味浓郁。 有些店家会再淋上肉燥和加上肉松、香菜、萝卜干。",
    " 咸酥鸡 ": "咸酥鸡，或称盐酥鸡，是常见的台湾小吃之一，为台湾最常见的炸鸡块，特点是会加入九层塔一起油炸，带有特殊的香气。 盐酥鸡原本是鸡肉切成小块，先以酱料腌渍入味，再裹上油炸粉或调味过后的面粉浆，再油炸的料理，因后来材料的增加，现在盐酥鸡往往是一个各种炸物综合性的全称，常见的有花椰菜、杏鲍菇、鸡皮、四季豆、银丝卷等。",
    "鲜肉馄饨": "鲜肉馄饨 ，别名鲜肉抄手，是一道以肥瘦猪肉，小麦面粉，荠菜，干紫菜作为主要食材，料酒、盐、胡椒粉、香油作为调料制作而成的食品。",
    "葱油拌面": "葱油拌面是一道以面条、食用油、黄瓜丝、葱、姜、盐、鸡精、酱油、白糖、料酒、桂皮、大料作为食材制作而成的家常面食。 通常是将煮熟的面条放上葱油一起拌着吃。 葱油拌面是上海招牌美食，面条有韧劲又滑爽，品种包括开洋葱油面、葱油肉丝面、葱油三虾面。",
    " 腌笃鲜 ": "腌肚鲜是徽菜、苏帮菜、上海菜、杭帮菜的一种春季时令菜式，用冬笋、咸肉、豆腐皮结和鲜猪肉，置于文火上慢炖。此菜适合家庭制作，讲究原汁原味，无需添加盐、味精等任何调料。",
    " 条头糕 ": "条头糕是江沪地区传统特色糕点，是糯米粉糅合细沙做成长条状。 撒上桂花末更好吃。 作为江南点心一大特色，清代苏州文士顾禄所著的《清嘉录》中提到了条头糕。 二十世纪三十年代，夏衍在《懒寻旧梦录》里也写到：“那时候学校里是可以向校役订点心的，如条头糕、麻酥糖之类”。",
    " 粢饭糕 ": "粢饭糕（拼音：zī fàn gāo）是一种流行于江南一带的传统小吃，属油炸类糕点，因其做法也可称为油氽粢饭糕，南方其他地区称之为炸糍粑。粢饭糕外层呈金黄色，内层为雪白的软糯糍饭，咬起来喷香松脆。",
    "  锅贴  ": "锅贴，中国著名传统小吃，属于煎烙煮馅类食品。制作精巧，味道可口。根据季节配以不同鲜蔬菜。锅贴的形状各地不同，一般是细长饺子形状，但天津锅贴类似褡裢火烧。",
    " 八宝鸭 ": "八宝鸭是苏州、上海一带的一道特色传统名菜，属于沪菜、苏菜，八宝鸭是用带骨鸭开背，填入配料，扣在大碗里，封以玻璃纸蒸熟，鸭形丰腴饱满，原汁突出，出笼时再浇上用蒸鸭原卤调制的虾仁和青豆，满堂皆香。",
    "  熏鱼  ": "熏鱼主要产自江苏、浙江、上海一带，作为当地过年必备的食品，温中补虚，有利湿、暖胃和平肝、祛风等功效。明代《宋氏养生部》中详细记载：“治鱼为大轩，微腌，焚砻谷糠，熏熟燥。治鱼微腌，油煎之，日暴之，始烟熏之。”",
    "红烧猪蹄": "红烧猪蹄  红烧猪蹄是一道传统的名菜，也是一道比较常见的家常菜，以猪蹄为主要食材，这道菜味道可口，营养价值丰富，具有美容养颜、抗衰老、促进生长、改善冠心病等功效。",
    " 荔枝肉 ": "荔枝肉是福建省福州市等地的一道特色传统名菜，属于闽菜系；该菜品已有二三百年历史。因原料中有白色的荸荠和切成十字花刀的猪肉，烹调后因外形型似荔枝而得名。"

}


pureFoods = {

    " 胡辣汤 ": "胡辣汤，是中国河南、陕西等地的汤类食品。 常作为早餐，其特点是麻辣鲜香，食用时常搭配油条、包子等其它早点。",
    " 肉夹馍 ": "肉夹馍的叫法源自古汉语，是一种宾语前置，其意为“肉夹在馍中”，好吃实惠。",
    " 锅包肉 ": "锅包肉（英文名：Fried Pork in Scoop），光绪年间始创自哈尔滨道台府府尹杜学瀛厨师郑兴文之手。 成菜后，色泽金黄，口味酸甜。 锅包肉是为适应外宾口味，把咸鲜口味的“焦烧肉条”改成了一道酸甜口味的菜肴。",
    " 小龙虾 ": "麻辣小龙虾又名口味虾、长沙口味虾、香辣小龙虾，是湖南著名的地方小吃。 麻辣小龙虾以小龙虾为主材，配以辣椒、花椒和其他香辛料制成。成菜后，色泽红亮，口味辣并鲜香。",
    "重庆火锅": "重庆火锅，又称毛肚火锅或麻辣火锅，是中国传统饮食方式之一；以“辣、麻、咸、鲜、香、脆”为其口味，具有菜品多样、调味独特、吃法豪放等特点",
    " 碗仔翅 ": "碗仔翅是一種香港街頭仿魚翅羹小吃[1]，其材料以粉絲為主，以澱粉將湯煮至濃稠，並加入老抽和生抽成棕色，冬菇絲和雞肉絲常被加入一起烹調，使湯羹的口感更為充實。進食碗仔翅時，可按個人喜好加入麻油、浙醋、白胡椒粉或辣椒油調味",
    "  虾饺  ": "虾饺是广东省广州市的一种特色小吃，属于粤菜系，该菜品始创于20世纪初广州市郊伍村五凤乡的一间家庭式小茶楼，已经有百年历史；传统的虾饺是半月形、蜘蛛肚共有十二褶的，馅料有虾，有肉，有笋，味道鲜美爽滑，美味可口。",

    " 东坡肉 ": "宋人东坡先生的那首《猪肉颂》：“黄州有好肉，价钱如泥土，贵者不肯吃，贫者不解煮”。",
    "咖喱鱼蛋": "咖喱鱼蛋是一道地方小吃，属于闽菜、粤菜。口感弹牙，鲜嫩，海鲜味十足。因酱料不同有甜辣、酸甜等各种口味。咖喱鱼蛋是用特种咖喱粉及各种秘制酱料，将正宗的潮汕鱼丸、台湾鱼丸或者福建鱼丸在锅中煮，待鱼丸煮熟后盛出淋上甜辣酱或蕃茄酱等，可食用。",
    " 白切鸡 ": "白切鸡始于清代，因烹制时不加调味白煮而成以保持原味，肉质刚熟不烂且食用时随吃随斩，故又称“白斩鸡”。 白切鸡色泽洁白油黄，皮爽肉滑骨香，原汁原味，清淡鲜美。",

    " 红烧肉 ": "一道著名的大众菜肴，各大菜系都有自己特色的红烧肉。其以五花肉为制作主料，也可用猪后腿代替，最好选用肥瘦相间的三层肉来做，锅具以砂锅为主，做出来的肉肥瘦相间，肥而不腻，香甜松软，营养丰富，入口即化。",
    " 小笼包 ": "小笼包，是一种诞生于中国江南地区的著名点心，吴语区以外又称小笼包，多处地方亦盛行，例如广东、香港、台湾，以“体小、馅大、汁多、味鲜、皮薄、形美”而著称。 汤包源于北宋京城开封的灌汤包，现代形式的小笼包起源于江南，后又在各地得到发展和演变，形成不同的口味。",
    " 热干面 ": "热干面色泽黄而油润，味道鲜美，由于热量高，也可以当作主食，营养早餐，补充人体所需的能量。是武汉最出名的小吃之一。",
    "羊肉泡馍": "羊肉泡馍，亦称羊肉泡，古称“羊羹”，关中汉族风味饭食，源自西周。它烹制精细，料重味醇，肉烂汤浓，肥而不腻，营养丰富，香气四溢，诱人食欲，食后回味无穷。",
    " 钵钵鸡 ": "钵钵鸡是一种四川传统名小吃，属于川菜系。从清代流传至今已有上百年的历史。是以陶器钵盛放配以麻辣为主的佐料，加上多种调料的去骨鸡片拌和而成。有皮脆肉嫩，麻辣鲜香，甜咸适中的特色",
    "糖醋排骨": "糖醋排骨是川菜糖醋味型中具有代表性的一道大众喜爱的传统菜，因为口味香脆酸甜，颇受江浙沪人士喜爱。",
    " 豆腐脑 ": "豆腐脑又称水豆腐，是一道著名的传统特色小吃。利用大豆蛋白制成的高营养食品，多在晨间出售，常与豆腐花、豆花混用，依据各地口味不同，北方多爱咸食，而南方则偏爱甜味，亦有地区如四川等喜爱酸辣口味。",
    "  饺子  ": "饺子  初名馄饨，又有角子、角儿、匾食、扁食、牢丸、粉角、饺饵、水饺饵、水点心、水饺子、饺儿等多种称呼。饺子的烹饪方法多样，有煮、蒸、煎、烤等。自宋代开始，有了冬至日吃饺子的习俗，自明朝以来有了正月初一吃饺子的习俗。",
    "玉米排骨汤": "玉米排骨汤 是一道食补汤品，主要食材是玉米和排骨，主要烹饪工艺是炖。玉米可降低血液胆固醇浓度并防止其沉积于血管壁，营养丰富，促进人们对维生素和钙的吸收。",
    " 粉蒸肉 ": "粉蒸肉 ，亦称米粉肉，发源于江西。诗人袁枚在《随园食单》中首次记载为一道江西菜品，流行于中国南方（四川、江西、湖南、安徽、湖北、浙江、福建、广东梅州等地 ），所需材料主要是米粉和肉，烹饪方式是蒸。 属赣菜系",
    " 大闸蟹 ": "大闸蟹是中国传统的名贵、出口水产品之一。肉质细嫩，滋味鲜美，营养价值极高，所含蛋白质与海蟹相等，比鲫鱼要高；所含脂肪和碳水化合物远远高于沼虾、对虾、带鱼等；维生素A非常丰富，含铁质特别高，核黄素含量也多，属高级营养食品。",
    " 清蒸鱼 ": "清蒸鱼是用各类鱼制作的一道家常菜，主要原材料有鱼、生姜、香蒜等，口味咸鲜，鱼肉软嫩，鲜香味美，汤清味醇，具有养血和开胃的功效，是舌尖上的美食。",
    "红烧狮子头": "红烧狮子头  ，是一道淮扬名菜。将有肥有瘦的肉配上荸荠，香菇等材料，做成丸子，然后先炸后煮",
    "章鱼丸子": "章鱼丸子是一种美食，主要材料有章鱼、海苔、高丽菜等，起源于日本，特点制作简单，口味独特，口感鲜嫩，工艺性较强，深受欢迎。",
    "    肉燕    ": "肉燕别称扁肉燕。但是肉燕皮是由猪肉加番薯粉手工打制而成。是福州一大特色小吃，肉燕有别于福建其他地区的扁肉（扁食），两者口感是完全不一样的。燕皮薄如白纸，其色似玉，口感软嫩，韧而有劲。",
    "油焖大虾": "油焖大虾是山东省的一道特色名菜，属于鲁菜。该菜品的主要食材为清明前渤海湾的大对虾，使用鲁菜特有的油焖技法。其是一道历史悠久的名菜，鲜香甜咸四种味道相辅相成，回味无穷。",
    " 毛血旺 ": "毛血旺是川菜的一道特色名菜，也是重庆江湖菜的鼻祖之一，已经列入国家标准委员会《渝菜烹饪标准体系》。毛血旺以鸭血为制作主料，烹饪技巧以煮菜为主，口味属于麻辣味。其起源于重庆，流行于西南地区，是一道著名的传统菜式，这道菜是将生血旺现烫现吃，且毛肚杂碎为主料，遂得名。",
    "可乐鸡翅": "可乐鸡翅具有味道鲜美、色泽艳丽、鸡肉嫩滑、咸甜适中的特点。一般人群均可食用，不适合感冒发热、内火偏旺、痰湿偏重的人。患有热毒疖肿、高血压、血脂偏高、胆囊炎、胆石症、糖尿病患者忌食。",
    " 腊八粥 ": "腊八粥，又称七宝五味粥、佛粥、大家饭等，是一种由多样食材熬制而成的粥。“喝腊八粥”是腊八节的习俗，腊八粥的传统食材包括大米、小米、玉米、薏米、红枣、莲子、花生、桂圆和各种豆类",
    "宫保鸡丁": "宫保鸡丁是一道闻名中外的特色传统名菜，在鲁菜、川菜、贵州菜中都有收录，其原料、做法有差别。该菜式的起源与鲁菜中的酱爆鸡丁、贵州菜中的胡辣子鸡丁有关，后被清朝山东巡抚、四川总督丁宝桢改良发扬，形成了一道新菜式——宫保鸡丁，并流传，此道菜也被归纳为北京宫廷菜。之后宫保鸡丁也流传到国外",
    " 回锅肉 ": "回锅肉，是四川传统菜式中家常菜肴的代表菜之一，属于川菜。其制作原料主要有猪后臀肉（二刀肉）、青椒、蒜苗等，口味独特，色泽红亮，肥而不腻。",
    "北京烤鸭": "北京烤鸭是起源于南北朝时期的宫廷名菜，用优质肉食鸭，果木炭火烤制，色泽红润，肉质肥而不腻，外脆里嫩，肉质细腻、味道醇厚1。北京烤鸭分为两大流派，即全聚德和便宜坊，它们都以色泽红艳、肉质细嫩、味道醇厚、肥而不腻的特色而著名。正宗北京烤鸭的食材和调料包括京白鸭、馒头等。吃法有三种，可以将鸭肉卷在薄饼里配以葱、黄瓜、甜面酱等，也可以直接食用鸭肉，还可以将鸭骨熬成汤",
    "草莓蛋糕卷": "草莓蛋糕卷是一道美食，主料是中筋面粉、蛋，配料是温牛奶、草莓粉，调料为白醋等，主要通过烘烤的方法制作而成。",
    " 肠仔包 ": "肠仔包，是一种美味又可口的食物，带有葱香味的美味肠仔包，柔软咸香的口感，且不宜多食。",
    "珍珠奶茶": "珍珠奶茶，又称波霸奶茶（英语：Boba milk tea）、泡泡茶，是1980年代起源于台湾的茶类饮料，为台湾泡沫红茶、粉圆茶饮文化中的分支，其作法为将粉圆加入奶茶中，奶茶可以是由奶精或鲜乳调制；另有“珍珠红（绿）茶”、“珍珠奶绿”等衍生种类，为台湾最具代表性的手摇饮料之一，并从台湾流行至世界各地。",
    "冬阴功汤": "冬阴功汤，是泰国和老挝的一道富有特色的酸辣口味汤品。也叫作东炎汤，在泰国非常普遍。主要食材有柠檬叶、香茅、虾等。",
    " 蚵仔煎 ": "蚵仔煎是一道聞名於臺灣的小吃，在新加坡、馬來西亞類似為蠔煎，而在福建、潮汕地區有海蠣煎。差別在於臺灣的加入地瓜粉、太白粉，新加坡、馬來西亞以蛋為主，而福建、潮汕則以麵粉摻入為主。",
    "生煎馒头": "生煎馒头是流行于上海、苏州及其他江南地区的一种传统小吃，简称为生煎；亦称生煎包，类似于锅贴和水煎包，为煎熟了的有馅馒头（包子）。 生煎馒头的馅料通常使用猪肉，也可用鸡肉作原料，在一些考究的店家研发了虾肉、蟹肉等馅料。",
    "大肠包小肠": "大肠包小肠是台湾一种小吃，发源于台湾花莲的客家人出门工作时的点心，于公元一九九零年代开始在台湾夜市流行，并在现在成为台湾普遍的美食。在许多景点常有小摊贩与客人以骰子对赌，故有句俗谚曰“黑无肠，白无肠，大肠包小肠”。大肠包小肠与美国的热狗有异曲同工之妙。",
    "筒仔米糕": "筒仔米糕是一样常见于糯米类小吃，与油饭、米糕类似，但却是在瓷瓶、竹筒或铁罐中炊煮而成，口味浓郁。 有些店家会再淋上肉燥和加上肉松、香菜、萝卜干。",
    " 咸酥鸡 ": "咸酥鸡，或称盐酥鸡，是常见的台湾小吃之一，为台湾最常见的炸鸡块，特点是会加入九层塔一起油炸，带有特殊的香气。 盐酥鸡原本是鸡肉切成小块，先以酱料腌渍入味，再裹上油炸粉或调味过后的面粉浆，再油炸的料理，因后来材料的增加，现在盐酥鸡往往是一个各种炸物综合性的全称，常见的有花椰菜、杏鲍菇、鸡皮、四季豆、银丝卷等。",
    "鲜肉馄饨": "鲜肉馄饨 ，别名鲜肉抄手，是一道以肥瘦猪肉，小麦面粉，荠菜，干紫菜作为主要食材，料酒、盐、胡椒粉、香油作为调料制作而成的食品。",
    "葱油拌面": "葱油拌面是一道以面条、食用油、黄瓜丝、葱、姜、盐、鸡精、酱油、白糖、料酒、桂皮、大料作为食材制作而成的家常面食。 通常是将煮熟的面条放上葱油一起拌着吃。 葱油拌面是上海招牌美食，面条有韧劲又滑爽，品种包括开洋葱油面、葱油肉丝面、葱油三虾面。",
    " 腌笃鲜 ": "腌肚鲜是徽菜、苏帮菜、上海菜、杭帮菜的一种春季时令菜式，用冬笋、咸肉、豆腐皮结和鲜猪肉，置于文火上慢炖。此菜适合家庭制作，讲究原汁原味，无需添加盐、味精等任何调料。",
    " 条头糕 ": "条头糕是江沪地区传统特色糕点，是糯米粉糅合细沙做成长条状。 撒上桂花末更好吃。 作为江南点心一大特色，清代苏州文士顾禄所著的《清嘉录》中提到了条头糕。 二十世纪三十年代，夏衍在《懒寻旧梦录》里也写到：“那时候学校里是可以向校役订点心的，如条头糕、麻酥糖之类”。",
    " 粢饭糕 ": "粢饭糕（拼音：zī fàn gāo）是一种流行于江南一带的传统小吃，属油炸类糕点，因其做法也可称为油氽粢饭糕，南方其他地区称之为炸糍粑。粢饭糕外层呈金黄色，内层为雪白的软糯糍饭，咬起来喷香松脆。",
    "  锅贴  ": "锅贴，中国著名传统小吃，属于煎烙煮馅类食品。制作精巧，味道可口。根据季节配以不同鲜蔬菜。锅贴的形状各地不同，一般是细长饺子形状，但天津锅贴类似褡裢火烧。",
    " 八宝鸭 ": "八宝鸭是苏州、上海一带的一道特色传统名菜，属于沪菜、苏菜，八宝鸭是用带骨鸭开背，填入配料，扣在大碗里，封以玻璃纸蒸熟，鸭形丰腴饱满，原汁突出，出笼时再浇上用蒸鸭原卤调制的虾仁和青豆，满堂皆香。",
    "  熏鱼  ": "熏鱼主要产自江苏、浙江、上海一带，作为当地过年必备的食品，温中补虚，有利湿、暖胃和平肝、祛风等功效。明代《宋氏养生部》中详细记载：“治鱼为大轩，微腌，焚砻谷糠，熏熟燥。治鱼微腌，油煎之，日暴之，始烟熏之。”",

    " 荔枝肉 ": "荔枝肉是福建省福州市等地的一道特色传统名菜，属于闽菜系；该菜品已有二三百年历史。因原料中有白色的荸荠和切成十字花刀的猪肉，烹调后因外形型似荔枝而得名。"

}
knight = 1137930693620543633
fairy = 1137930658489053184
lwbb = 1111868751990763652
warning = 1111868751990763652
# ink: 926619981981044747
