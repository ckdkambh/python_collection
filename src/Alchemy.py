# coding=UTF-8

L = '''
1. 1UP（原版未翻译，理解为《超级玛丽》中的“加命蘑菇”）← life（生活，应理解为生命）+ mushroom（蘑菇）
　　
　　2. air（空气，基本元素）
　　
　　3. airplane（原版未翻译，译为飞机）← metal（金属）+ bird（鸟）
　　
　　4. alcohol（酒，应理解为酒精）← fire（火）+ water（水）
　　
　　5. alcoholic（酒精，应理解为酗酒）← alcohol（酒，应理解为酒精）+ man（人类）
　　
　　6. algae（藻类）← life（生活，应理解为生命）+ water（水）
　　
　　7. arable（耕地）← earth（土）+ tool（工具）
　　
　　8. arms（武器）← metal（金属）+ tool（工具）
　　
　　9. ash（灰）← air（空气）+ earth（土）
　　
　　10. ashtray（烟灰缸）← ash（灰）+ glass（玻璃）
　　
　　11. assassin（刺客）← man（人类）+ poisoned weapon（有毒武器）
　　
　　12. avian flu（原版未翻译，译为禽流感）← flu（流感）+ bird（鸟）
　　
　　13. bacon（熏肉）← pig（猪）+ fire（火）
　　
　　14. bacteria（菌）← life（生活，应理解为生命）+ swamp（沼泽）
　　
　　15. bar（原版未翻译，译为酒吧）← beer（啤酒）+ brick house（砖房）
　　
　　16. barbecue（烧烤）← fire（火）+ meat（肉类）
　　
　　17. bat（蝙蝠）← bird（鸟）+ vampire（吸血鬼）
　　
　　18. Batman（勤务兵，应理解为蝙蝠侠）← bat（蝙蝠）+ man（人类）
　　
　　19. beach（海滩）← sand（沙）+ water（水）
　　
　　20. bear（熊）← beast（兽）+ forest（林木，应理解为森林）
　　
　　21. beast（兽）← lizard（蜥蜴）+ earth（土）
　　
　　22. beaver（海狸）← beast（兽）+ dam（母兽，应理解为水坝）
　　
　　23. beer（啤酒）← alcohol（酒，应理解为酒精）+ wheat（小麦）
　　
　　24. beetle（甲虫）← earth（土）+ worm（蠕虫）
　　
　　25. berry（原版未翻译，译为浆果）← fruit（原版未翻译，译为水果）+ grass（草）
　　
　　26. bicycle（自行车）← wheel（轮）+ wheel（轮）
　　
　　27. bird（鸟）← egg（鸡蛋，应理解为卵）+ air（空气）
　　
　　28. bitumen（沥青）← kerogen（油母页岩）+ pressure（压力）
　　
　　29. blood（血）← dinosaur（恐龙）+ man（人类）
　　
　　30. boat（船）← water（水）+ wood（木）
　　
　　31. boiler（锅炉）← metal（金属）+ steam（蒸汽）
　　
　　32. book（书）← paper（纸）+ feather（羽毛）
　　
　　33. bread（面包）← dough（生面团）+ fire（火）
　　
　　34. brick（砖）← fire（火）+ clay（粘土）
　　
　　35. brick house（砖房）← brick（砖）+ concrete（混凝土）
　　
　　36. butterfly（蝴蝶）← air（空气）+ worm（蠕虫）
　　
　　37. cactus（仙人掌）← desert（沙漠）+ tree（树）
　　
　　38. car（汽车）← cart（车）+ combustion engine（内燃机）
　　
　　39. caramel（焦糖）← sugar（糖）+ fire（火）
　　
　　40. carbon dioxide（二氧化碳）← oxygen（氧）+ man（人类）
　　
　　41. carmine（深红色）← cochineal（胭脂虫）+ fire（火）
　　
　　42. cart（车）← wheel（轮）+ wood（木）
　　
　　43. caviar（鱼子酱）← fish（鱼）+ egg（鸡蛋，应理解为卵）
　　
　　44. cement（水泥）← clay（粘土）+ limestone（石灰石）
　　
　　45. cemetery（墓地）← grave（坟墓）+ grave（坟墓）
　　
　　46. ceramics（陶瓷）← man（人类）+ clay（粘土）
　　
　　47. champagne（原版未翻译，译为香槟）← wine（原版未翻译，译为葡萄酒）+ carbon dioxide（二氧化碳）
　　
　　48. iot（双轮战车）← warrior（战士）+ cart（车）
　　
　　49. cheese（奶酪）← milk（牛奶）+ mold（模型）
　　
　　50. chicken（鸡肉，应理解为鸡）← egg（鸡蛋，应理解为卵）+ life（生活，应理解为生命）
　　
　　51. Christmas tree（圣诞树）← light bulb（白炽灯，应理解为灯泡）+ tree（树）
　　
　　52. cigarettes（香烟）← paper（纸）+ tobacco（烟草）
　　
　　53. city（城市）← skyscraper（摩天楼）+ skyscraper（摩天楼）
　　
　　54. clay（粘土）← sand（沙）+ swamp（沼泽）
　　
　　55. cloth（布）← tool（工具）+ wool（羊毛）
　　
　　56. clothing（服装）← cloth（布）+ man（人类）
　　
　　57. cloud（原版未翻译，译为云）← air（空气）+ steam（蒸汽）
　　
　　58. coal（煤）← fire（火）+ wood（木）
　　
　　59. Coca-Cola（可口可乐）← carmine（深红色）+ soda water（苏打水）
　　
　　60. cochineal（胭脂虫）← beetle（甲虫）+ cactus（仙人掌）
　　
　　61. coffin（灵柩）← corpse（尸体）+ wood（木）
　　
　　62. combustion engine（内燃机）← gasoline（汽油）+ steam-engine（蒸汽引擎）
　　
　　63. concrete（混凝土）← cement（水泥）+ water（水）
　　
　　64. corpse（尸体）← fire（火）+ man（人类）
　　
　　65. dam（母兽，应理解为水坝）← brick（砖）+ water（水）
　　
　　66. desert（沙漠）← sand（沙）+sand（沙）
　　
　　67. diamond（钻石）← uncut diamond（未切割钻石）+ tool（工具）
　　
　　68. diet（原版未翻译，译为节食）← man（人类）+ yogurt（酸奶）
　　
　　69. dinosaur（恐龙）← egg（鸡蛋，应理解为卵）+ earth（土）
　　
　　70. dough（生面团）← flour（面粉）+ water（水）
　　
　　71. dragon（龙）←fire（火）+ dinosaur（恐龙）
　　
　　72. dust（尘土）← air（空气）+ earth（土）
　　
　　73. earth（土，基本元素）
　　
　　74. ectoplasm（外质）← energy（能源）+ ghost（幽灵）
　　
　　75. egg（鸡蛋，应理解为卵）← stone（石）+ life（生活，应理解为生命）
　　
　　76. electric eel（电鳗）← electricity（电）+ snake（蛇）
　　
　　77. electric ray（电鳐）← electricity（电）+ fish（鱼）
　　
　　78. electricity（电）← energy（能源）+metal（金属）
　　
　　79. energy（能源）← fire（火）+ air（空气）
　　
　　80. explosion（爆炸）← fire（火）+ gunpowder（火药）
　　
　　81. farmer（农夫）← man（人类）+ seed（种子）
　　
　　82. fat（脂肪）← man（人类）+ pig（猪）
　　
　　83. feather（羽毛）← hunter（猎人）+ bird（鸟）
　　
　　84. fern（蕨类）← moss（苔）+ swamp（沼泽）
　　
　　85. fire（火，基本元素）
　　
　　86. fire elemental（火元素）← fire（火）+ life（生活，应理解为生命）
　　
　　87. firearms（枪械）← arms（武器）+ gunpowder（火药）
　　
　　88. firefighter（消防队员）← fire（火）+ hero（英雄）
　　
　　89. firefly（萤火虫）← light（光）+ beetle（甲虫）
　　
　　90. fish（鱼）← snake（蛇）+ water（水）
　　
　　91. fisherman（渔船，应理解为渔夫）← fish（鱼）+ hunter（猎人）
　　
　　92. flour（面粉）← wheat（小麦）+ stone（石头）
　　
　　93. flower（原版未翻译，译为花）← water（水）+seed（种子）
　　
　　94. flu（流感）← air（空气）+ bacteria（菌）
　　
　　95. flying dinosaur（飞行恐龙）← dinosaur（恐龙）+ air（空气）
　　
　　96. fondue（干酪）← cheese（奶酪）+ fire（火）
　　
　　97. forest（林木，应理解为森林）← grove （小树林）+ grove（小树林）
　　
　　98. fossil（化石）← dinosaur（恐龙）+ earth（土）
　　
　　99. Frankenstein（法兰肯斯坦）← corpse（尸体）+ electricity（电）
　　
　　100. frog（青蛙）← lizard（蜥蜴）+ swamp（沼泽）
　　
　　101. fruit（原版未翻译，译为水果）← flower（原版未翻译，译为花）+ tree（树）
　　
　　102. gasoline（汽油）← petroleum（石油）+ pressure（压力）
　　
　　103. genie（妖怪，即阿拉伯灯神）← ghost（幽灵）+ lamp（灯）
　　
　　104. geyser（喷泉）← earth（土）+ steam（蒸汽）
　　
　　105. ghost（幽灵）← ash（灰）+ life（生活，应理解为生命）
　　
　　106. glass（玻璃）← fire（火）+ sand（沙）
　　
　　107. golem（魔像）← clay（粘土）+ life（生活，应理解为生命）
　　
　　108. grape（原版未翻译，译为葡萄）← earth（土）+ wood（木）
　　
　　109. grass（草）← moss（苔）+ earth（土）
　　
　　110. grave（坟墓）← coffin（灵柩）+ earth（土）
　　
　　111. grove（小树林）← tree（树）+ tree（树）
　　
　　112. gunpowder（火药）← dust（尘土）+ fire（火）
　　
　　113. hen coop（鸡舍）← chicken（鸡肉，应理解为鸡）+ hut（棚屋）
　　
　　114. hero（英雄）← dragon（龙）+ warrior（战士）
　　
　　115. hospital（医院）← brick house（砖房）+ sick（呕吐物，应理解为患病）
　　
　　116. hourglass（玻璃）← glass（玻璃）+ sand（沙）
　　
　　117. hunter（猎人）← man（人类）+ arms（武器）
　　
　　118. hut（棚屋）← man（人类）+ stone（石）
　　
　　119. hydrogen（氢）← electricity（电）+ water（水）
　　
　　120. idea（计划，应理解为主意）← light bulb（白炽灯，应理解为灯泡）+ man（人类）
　　
　　121. iodine（碘）← algae（藻类）+ fire（火）
　　
　　122. Kama Sutra（卡马经，即印度《爱经》）← book（书）+ sex（性别，应理解为性）
　　
　　123. kerogen（油母页岩）← fossil（化石）+ pressure（压力）
　　
　　124. knife（小刀）← meat（肉类）+ tool（工具）
　　
　　125. lamp（灯）← fire（火）+glass（玻璃）
　　
　　126. lava（岩浆）← fire（火）+ earth（土）
　　
　　127. lava golem（熔岩魔像）← lava（岩浆）+ life（生活，应理解为生命）
　　
　　128. lava lamp（熔岩灯）←lava（岩浆）+ lamp（灯）
　　
　　129. leech（水蛭）← blood（血）+ worm（蠕虫）
　　
　　130. library（图书馆）← book（书）+ book（书）
　　
　　131. lichen（青苔）← algae（藻类）+ mushroom（蘑菇）
　　
　　132. life（生活，应理解为生命）← swamp（沼泽）+ energy（能源）
　　
　　133. light（光）← electricity（电）+ light bulb（白炽灯，应理解为灯泡）
　　
　　134. light bulb（白炽灯，应理解为灯泡）← electricity（电）+ glass（玻璃）
　　
　　135. lighthouse（灯塔）← light（光）+ skyscraper（摩天楼）
　　
　　136. lightning rod（原版未翻译，译为避雷针）← thunderstorm（大雷雨）+ metal（金属）
　　
　　137. lightsaber（原版未翻译，译为光剑，出自《星球大战》）← light（光）+ arms（武器）
　　
　　138. lime（石灰）← limestone（石灰石）+ fire（火）
　　
　　139. limestone（石灰石）← shells（炮弹，应理解为贝壳）+ stone（石）
　　
　　140. livestock（牲畜）← man（人类）+ beast（兽）
　　
　　141. lizard（蜥蜴）← egg（鸡蛋，应理解为卵）+ swamp（沼泽）
　　
　　142. locomotive（机车）← cart（车）+ steam-engine（蒸汽引擎）
　　
　　143. man（人类）← golem（魔像）+ life（生活，应理解为生命）
　　
　　144. manure（肥料）← grass（草）+ livestock（牲畜）
　　
　　145. Mario（马里奥，出自游戏《超级玛丽》）← 1UP（原版未翻译，理解为《超级玛丽》中的“加命蘑菇”）+ man（人类）
　　
　　146. McDonaldss（麦当劳，理解为McDonald’s）← sandwich（三明治）+ Coca-Cola（可口可乐）
　　
　　147. meat（肉类）← hunter（猎人）+ bird（鸟）
　　
　　148. metal（金属）← stone（石）+ fire（火）
　　
　　149. metal golem（金属魔像）← metal（金属）+ life（生活，应理解为生命）
　　
　　150. milk（牛奶）← livestock（牲畜）+ man（人类）
　　
　　151. mite（小蜘蛛）← dust（尘土）+ life（生活，应理解为生命）
　　
　　152. mold（模型）← mud（泥土）+ mushroom（蘑菇）
　　
　　153. Molotov cocktail（燃烧弹，即“莫洛托夫鸡尾酒”）← alcohol（酒，应理解为酒精）+ fire（火）
　　
　　154. moss（苔）← algae（藻类）+ swamp（沼泽）
　　
　　motorboat（汽艇）← combustion engine（内燃机）+ boat（船）
　　
　　156. motorcycle（摩托车）← combustion engine（内燃机）+ bicycle（自行车）
　　
　　157. mud（泥土）← dust（尘土）+ water（水）
　　
　　158. museum（博物馆）← brick house（砖房）+ fossil（化石）
　　
　　159. mushroom（蘑菇）← algae（藻类）+ earth（土）
　　
　　160. obesity（原版未翻译，译为过胖）← man（人类）+ McDonaldss（麦当劳，理解为McDonald’s）
　　
　　161. omelette（煎蛋卷）← egg（鸡蛋，应理解为卵）+ fire（火）
　　
　　162. oxygen（氧）← electricity（电）+ water（水）
　　
　　163. oxyhydrogen（氢氧混合气）← oxygen（氧）+ hydrogen（氢）
　　
　　164. ozone（原版未翻译，译为臭氧）← air（空气）+ electricity（电）
　　
　　165. panda（熊猫）← beast（兽）+ tree（树）
　　
　　166. paper（纸）← reed（芦苇）+ tool（工具）
　　
　　167. pearl（珍珠）← shells（炮弹，应理解为贝壳）+ sand（沙）
　　
　　168. peat（泥炭）← swamp（沼泽）+ tree（树）
　　
　　169. penicillin（盘尼西林）← scientist（科学家）+ mold（模型）
　　
　　170. Petri dish（培养皿）← glass（玻璃）+ bacteria（菌）
　　
　　171. petroleum（石油）← bitumen（沥青）+ pressure（压力）
　　
　　172. phoenix（凤凰）← bird（鸟）+ fire（火）
　　
　　173. pig（猪）← mud（泥土）+ livestock（牲畜）
　　
　　174. pillow（枕头）← feather（羽毛）+ cloth（布）
　　
　　175. Pinocchio（匹诺曹，一个童话人物）← wood（木）+ life（生活，应理解为生命）
　　
　　176. pizza（原版未翻译，译为比萨饼）← cheese（奶酪）+ dough（生面团）
　　
　　177. plankton（浮游生物）← bacteria（菌）+ water（水）
　　
　　178. plesiosauria（蛇颈龙亚目）← dinosaur（恐龙）+ water（水）
　　
　　179. poison（毒药）← mushroom（蘑菇）+ tool（工具）
　　
　　180. poisoned weapons（有毒武器）← poison（毒药）+ arms（武器）
　　
　　181. pressure（压力）← earth（土）+ earth（土）
　　
　　182. prisoner（原版未翻译，译为囚犯）← assassin（刺客）+ time（原版未翻译，译为时间）
　　
　　183. quark(cheese)（夸克（奶酪））← fire（火）+ soured milk（牛奶变酸）
　　
　　184. Quetzalcoatl（原版未翻译，译为羽蛇神，神话中的一个神祗）← snake（蛇）+ feather（羽毛）
　　
　　185. reed（芦苇）← grass（草）+ swamp（沼泽）
　　
　　186. rust（铁，应理解为铁锈）← metal（金属）+ water（水）
　　
　　187. sailboat（帆船）← cloth（布）+ boat（船）
　　
　　188. sailing ship（大帆船）← cloth（布）+ wooden ship（木船）
　　
　　189. sailor（水手）← man（人类）+ boat（船）
　　
　　190. salamander（蝾螈）← lizard（蜥蜴）+ fire（火）
　　
　　191. saltpeter（硝）← limestone（石灰石）+ manure（肥料）
　　
　　192. sand（沙）← stone（石）+ water（水）
　　
　　193. sand storm（沙暴）← sand（沙）+ storm（风暴）
　　
　　194. sandwich（三明治）← bread（面包）+ meat（肉类）
　　
　　195. scarab（圣甲虫）← beetle（甲虫）+ manure（肥料）
　　
　　196. scientist（科学家）← library（图书馆）+ man（人类）
　　
　　197. scissors（原版未翻译，译为剪刀）← knife（小刀）+ knife（小刀）
　　
　　198. scorpion（蝎）← beetle（甲虫）+ sand（沙）
　　
　　199. scotch whisky（理解为Scotch whisky，原版未翻译，译为苏格兰威士忌）← alcohol（酒，应理解为酒精）+ peat（泥炭）
　　
　　200. seed（种子）← sand（沙）+ life（生活，应理解为生命）
　　
　　201. sex（性别，应理解为性）← man（人类）+ man（人类）
　　
　　202. shells（炮弹，应理解为贝壳）← plankton（浮游生物）+ stone（石）
　　
　　203. sick（呕吐物，应理解为患病）← man（人类）+ flu（流感）
　　
　　204. silicon（原版未翻译，译为硅）← sand（沙）+ pressure（压力）
　　
　　205. sky（原版未翻译，译为天空）← cloud（原版未翻译，译为云）+ air（空气）
　　
　　206. skyscraper（摩天楼）← brick house（砖房）+ glass（玻璃）
　　
　　207. smoke（烟）← fire（火）+ gunpowder（火药）
　　
　　208. snail（蜗牛）← worm（蠕虫）+ shells（炮弹，应理解为贝壳）
　　
　　209. snake（蛇）← sand（沙）+ worm（蠕虫）
　　
　　210. sniper（狙击手）← assassin（刺客）+ firearms（枪械）
　　
　　211. soap（肥皂）← ash（灰）+ fat（脂肪）
　　
　　212. soda water（苏打水）← carbon dioxide（二氧化碳）+ water（水）
　　
　　213. soldier（士兵）← man（人类）+ firearms（枪械）
　　
　　214. soured milk（牛奶变酸）← yogurt（酸奶）+ milk（牛奶）
　　
　　215. spinning wheel（手纺车）← wheel（轮）+ wool（羊毛）
　　
　　216. stake（树桩）← wood（木）+ knife（小刀）
　　
　　217. star（原版未翻译，译为星）← Sun（原版未翻译，译为太阳）+ scientist（科学家）
　　
　　218. steam（蒸汽）← air（空气）+ water（水）
　　
　　219. steam-engine（蒸汽引擎）← coal（煤）+ boiler（锅炉）
　　
　　220. steamer（汽船）← steam-engine（蒸汽引擎）+ wooden ship（木船）
　　
　　221. stone（石）← lava（岩浆）+ water（水）
　　
　　222. storm（风暴）← air（空气）+ energy（能源）
　　
　　223. sugar（糖）← lime（石灰）+ reed（芦苇）
　　
　　224. sulfur（硫）← bacteria（菌）+ swamp（沼泽）
　　
　　225. Sun（原版未翻译，译为太阳）← sky（原版未翻译，译为天空）+ iot（双轮战车）[注：希腊神话中的太阳神驾驶太阳车行驶于天空]
　　
　　226. sushi（寿司）← algae（藻类）+ fish（鱼）
　　
　　227. swamp（沼泽）← earth（土）+ water（水）
　　
　　228. sweater（毛衣）← tool（工具）+ yarn（纱线）
　　
　　229. swine flu（猪流感）← flu（流感）+ pig（猪）
　　
　　230. team（团队）← beast（兽）+ cart（车）
　　
　　231. tequila（龙舌兰酒）← alcohol（酒，应理解为酒精）+ worm（蠕虫）
　　
　　232. thunderbird（鸟）← storm（风暴）+ bird（鸟）
　　
　　233. thunderstorm（雷鸟）← electricity（电）+ storm（风暴）
　　
　　234. time（时间）← life（生活，应理解为生命）+ hourglass（玻璃）
　　
　　235. toast（吐司）← bread（面包）+ fire（火）
　　
　　236. tobacco（烟草）← grass（草）+ fire（火）
　　
　　237. tool（工具）← man（人类）+ metal（金属）
　　
　　238. Totoro（龙猫，亦即多多洛，出自宫崎骏动画《龙猫》）← ghost（幽灵）+ forest（林木，应理解为森林）
　　
　　239. tree（树）← earth（土）+ seed（种子）
　　
　　240. turtle（龟）← egg（鸡蛋，应理解为卵）+ sand（沙）
　　
　　241. Twilight Saga（暮光之城）← werewolf（狼人）+ vampire（吸血鬼）
　　
　　242. typhoon（台风）← storm（风暴）+ water（水）
　　
　　243. uncut diamond（未切割钻石）← coal（煤）+ pressure（压力）
　　
　　244. undead（不死族）← corpse（尸体）+ zombie（僵尸）
　　
　　245. vampire（吸血鬼）← blood（血）+ man（人类）
　　
　　246. vinegar（原版未翻译，译为醋）← alcohol（酒，应理解为酒精）+ oxygen（氧）
　　
　　247. vodka（伏特加酒）← alcohol（酒，应理解为酒精）+ water（水）
　　
　　248. volcano（火山）← lava（岩浆）+ pressure（压力）
　　
　　249. vulture（秃鹰）← corpse（尸体）+ bird（鸟）
　　
　　250. VW Beetle（甲壳虫汽车）← beetle（甲虫）+ car（汽车）
　　
　　251. walking tree（走路的树）← tree（树）+ life（生活，应理解为生命）
　　
　　252. warrior（战士）← hunter（猎人）+ arms（武器）
　　
　　253. water（水，基本元素）
　　
　　254. weevil（象鼻虫）← flour（面粉）+ beetle（甲虫）
　　
　　255. werewolf（狼人）← beast（兽）+ vampire（吸血鬼）
　　
　　256. whale（鲸鱼）← beast（兽）+ water（水）
　　
　　257. wheat（小麦）← arable（耕地）+ seed（种子）
　　
　　258. wheel（轮）← wood（木）+ tool（工具）
　　
　　259. whey（乳水）← fire（火）+ soured milk（牛奶变酸）
　　
　　260. wind（风）← air（空气）+ air（空气）
　　
　　261. wine（原版未翻译，译为葡萄酒）← grape（原版未翻译，译为葡萄）+ alcohol（酒，应理解为酒精）
　　
　　262. wood（木）← tree（树）+ tool（工具）
　　
　　263. wooden ship（木船）← wood（木）+ boat（船）
　　
　　264. wool（羊毛）← beast（兽）+ hunter（猎人）
　　
　　265. worm（蠕虫）← earth（土）+ plankton（浮游生物）
　　
　　266. yarn（纱线）← spinning wheel（手纺车）+ wool（羊毛）
　　
　　267. yogurt（酸奶）← bacteria（菌）+ milk（牛奶）
　　
　　268. Yoshi（原版未翻译，《超级玛丽》游戏中的恐龙名）← 1UP（原版未翻译，理解为《超级玛丽》中的“加命蘑菇”）+ dinosaur（恐龙）
　　
　　269. zombie（僵尸）← corpse（尸体）+ life（生活，应理解为生命）
　　
　　270. zoo（原版未翻译，译为动物园）← beast（兽）+ museum（博物馆）
　　
　　271. aluminium（铝） = plane（平面） + metal（金属）
　　
　　272. bow = Robin Hood + arms
　　
　　273. cat（猫） = mouse（老鼠） + hunter（猎人）
　　
　　274. cancer（癌症） = man（人） + cigarette（香烟）
　　
　　275. continent（大陆） = ry（国家） + ry（国家）
　　
　　276. ry（国家） = city（城市） + city（城市）
　　
　　277. Faberge egg（彩蛋） = egg（蛋） + diamond（钻）
　　
　　278. fugu（河豚）= fish（鱼） + poison（毒药）
　　
　　279. Ghostbusters（捉鬼） = ghost（鬼） + hunter（猎人）
　　
　　280. ice（冰） = water（水） + glass（玻璃）
　　
　　281. jedi（武士） = warrior（战士） + light saber（军刀）
　　
　　282. juice（果汁） = fruit（水果） + pressure（打压）
　　
　　283. Lance Armstrong（阿姆斯特朗） = cancer（癌症） + bicycle（自行车）
　　
　　284. lawn mower（割草机） = tool（工具） + grass（草）
　　
　　285. Mentos（曼妥思） = geyser（喷泉） + Coca-Cola（可口可乐）
　　
　　286. mirror（镜子） = aluminium（铝） + glass（玻璃）
　　
　　287. Moon（月亮） = cheese（奶酪） + sky（天空）
　　
　　288. mouse（老鼠） = cheese（奶酪） + beast（捕捉器）
　　
　　289. mummy（木乃伊） = corpse（尸体） + cloth（衣服）
　　
　　290. old man（老男人） = time（时间） + man（男人）
　　
　　291. perfume（香水） = flower（花） + alcohol（酒精）
　　
　　292. Robin Hood（罗宾逊） = forest（森林） + hero（英雄）
　　
　　293. Santa Claus（圣诞老人） = old man（老男人） + christmas tree（圣诞树）
　　
　　294. Sex and the City（欲望都市） = sex（性爱） + city（城市）
　　
　　295. silver（银币） = Moon（月亮） + metal（金属）
　　
　　296. sith（西门子） = jedi（武士） + assasin（刺客）
　　
　　297. Star Wars（星球大战） = sith（西门子） + jedi（武士）
　　
　　298. sunflower（向日葵） = Sun（太阳） + flower（花）
　　
　　299. The Beatles（甲壳虫乐队） = beetle（甲壳虫） + beetle（甲壳虫）
　　
　　300. tractor（拖拉机） = lawn mower（割草机） + arable（耕地）
'''  
print(L)