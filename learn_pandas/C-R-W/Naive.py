# 访问操作
# 原生Python对象提供了索引数据的好方法。pandas把所有这些都带了过来，这使得它很容易开始。
# Consider this DataFrame:
import pandas as pd
reviews = pd.DataFrame({'country':['Italy','Portugal','France']})
#   country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 1	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit
# 129971 rows × 13 columns

# 在Python中，我们可以通过将对象作为属性访问来访问对象的属性。
# 例如，Book对象可能有一个title属性，我们可以通过调用book.title来访问该属性。
# 熊猫DataFrame中的列的工作方式大致相同。


print(reviews.country)
# 0            Italy
# 1         Portugal
#             ...
# 129969      France
# 129970      France
# Name: country, Length: 129971, dtype: object
# 如果我们有一个Python字典，我们可以使用索引([])操作符来访问它的值。
# 我们可以对DataFrame中的列执行相同的操作：

reviews['country']
# 0            Italy
# 1         Portugal
#             ...
# 129969      France
# 129970      France
# Name: country, Length: 129971, dtype: object
# 这是从DataFrame中选择特定系列的两种方式。它们在语法上都不是或多或少有效的，
# 但是索引操作符[]确实有一个优点，那就是它可以处理其中带有保留字符的列名(例如，
# 如果我们有一个COUNTRY PROVIDENS列，REVIEWS。COUNTRY PROVIDENSES将不起作用)。
# 熊猫丛书看起来是不是有点像一本花哨的字典？基本上是这样，因此，要深入到单个特定值，我们只需再次使用索引操作符[]就不足为奇了：
print(reviews['country'][0])
# 'Italy'


# Indexing in pandas
# 索引操作符和属性选择很好，因为它们的工作方式与Python生态系统的其余部分一样。
# 作为一个新手，这使得它们很容易拿起和使用。但是，熊猫有自己的访问器操作符loc和iloc。对于更高级的操作，这些是您应该使用的操作。
# Index-based selection
# 熊猫索引的工作方式有两种。第一种是基于索引的选择：根据数据中的数字位置选择数据。ILOC遵循这一范例。
# To select the first row of data in a DataFrame, we may use the following:

print(reviews.iloc[0])
# country                                                    Italy
# description    Aromas include tropical fruit, broom, brimston...
#                                      ...
# variety                                              White Blend
# winery                                                   Nicosia
# Name: 0, Length: 13, dtype: object
# Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.

# 这意味着检索行稍微容易一些，检索列稍微困难一点。要使用iloc获取一个专栏，我们可以执行以下操作：

reviews.iloc[:, 0]

# 0            Italy
# 1         Portugal
#             ...
# 129969      France
# 129970      France
# Name: country, Length: 129971, dtype: object
# 运算符：本身也来自原生Python，表示\“一切\”。但是，当与其他选择器结合使用时，它可以用来指示值的范围。例如，要仅从第一行、第二行和第三行选择Country列，我们将执行以下操作：
# reviews.iloc[:3, 0]
# 0       Italy
# 1    Portugal
# 2          US
# Name: country, dtype: object
# Or, to select just the second and third entries, we would do:

reviews.iloc[1:3, 0]
# 1    Portugal
# 2          US
# Name: country, dtype: object
# It's also possible to pass a list:

reviews.iloc[[0, 1, 2], 0]
# 0       Italy
# 1    Portugal
# 2          US
# Name: country, dtype: object
# 最后，值得知道的是，负数可以用于选择。这将从值的末尾开始向前计数。例如，下面是数据集的最后五个元素。
reviews.iloc[-5:]
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 129966	Germany	Notes of honeysuckle and cantaloupe sweeten th...	Brauneberger Juffer-Sonnenuhr Spätlese	90	28.0	Mosel	NaN	NaN	Anna Lee C. Iijima	NaN	Dr. H. Thanisch (Erben Müller-Burggraef) 2013 ...	Riesling	Dr. H. Thanisch (Erben Müller-Burggraef)
# 129967	US	Citation is given as much as a decade of bottl...	NaN	90	75.0	Oregon	Oregon	Oregon Other	Paul Gregutt	@paulgwine	Citation 2004 Pinot Noir (Oregon)	Pinot Noir	Citation
# 129968	France	Well-drained gravel soil gives this wine its c...	Kritt	90	30.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Gresser 2013 Kritt Gewurztraminer (Als...	Gewürztraminer	Domaine Gresser
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit
# Label-based selection
# 属性选择的第二个范例是loc操作符遵循的范例：基于标签的选择。在这个范例中，重要的是数据索引值，而不是它的位置。
# For example, to get the first entry in reviews, we would now do the following:

reviews.loc[0, 'country']
# 'Italy'
# Iloc在概念上比loc简单，因为它忽略了数据集的索引。当我们使用iloc时，
# 我们将数据集视为一个大矩阵(列表列表)，我们必须按位置对其进行索引。
# 相比之下，LoC使用指数中的信息来开展工作。由于您的数据集通常具有有意义的索引，
# 因此使用loc通常更容易完成任务。例如，这里有一个使用loc会容易得多的操作：
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
#           taster_name	     taster_twitter_handle	points
# 0	         Kerin O’Keefe	 @kerinokeefe	        87
# 1	         Roger Voss	     @vossroger	            87
# ...	...	...	...
# 129969	 Roger Voss	     @vossroger	            90
# 129970	 Roger Voss	     @vossroger	            90
# 129971 rows × 3 columns

# Choosing between loc and iloc
# 在loc和iloc之间选择或转换时，有一个“问题”值得记住，那就是这两种方法使用的索引方案略有不同。

# Iloc使用Python stdlib索引方案，其中包括范围的第一个元素，排除最后一个元素。
# 因此，0：10将选择条目0、...、9.loc，同时包含索引。因此，0：10将选择条目0、...、10。

# 为什么要改呢？请记住，loc可以索引任何stdlib类型：例如字符串。
# 如果我们的DataFrame具有索引值Apples，...，马铃薯，...，并且我们想要选择
# \“苹果和土豆之间所有按字母顺序的水果选择\”，那么索引df.loc[‘Apples’：‘Potatos’]
# 要比索引df.loc[‘Apples’，‘Potatoet](不在字母表中的s后面)要方便得多。

# 当DataFrame索引是简单的数字列表(例如0、...、1000)时，这尤其令人困惑。
# 在本例中，df.iloc[0：1000]将返回1000个条目，而df.loc[0：1000]将返回1001个条目！
# 要使用loc获取1000个元素，您需要再低一个，然后请求df.loc[0：999]。

# 否则，使用loc的语义与使用iloc的语义相同。

# Manipulating the index
# 基于标签的选择的力量来自索引中的标签。关键的是，我们使用的索引并不是一成不变的。
# 我们可以用我们认为合适的任何方式来操纵索引。

# 可以使用set_index()方法来执行该工作。下面是将_index设置为Title字段时发生的情况：

reviews.set_index("title")
#                                   country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	variety	winery
# title
# Nicosia 2013 Vulkà Bianco (Etna)	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	White Blend	Nicosia
# Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Portuguese Red	Quinta dos Avidagos
# ...	...	...	...	...	...	...	...	...	...	...	...	...
# Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Pinot Gris	Domaine Marcel Deiss
# Domaine Schoffit 2012 Lieu-dit Harth Cuvée Caroline Gewurztraminer (Alsace)	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Gewürztraminer	Domaine Schoffit
# 129971 rows × 12 columns

# This is useful if you can come up with an index for the dataset which is better than the current one.

# Conditional selection
# 到目前为止，我们已经使用DataFrame本身的结构属性为各种数据编制了索引。
# 然而，要对数据做有趣的事情，我们通常需要根据条件提出问题。

# 例如，假设我们对意大利出产的高于平均水平的葡萄酒特别感兴趣。

# 我们可以从检查每种酒是否都是意大利酒开始：

reviews.country == 'Italy'
# 0          True
# 1         False
#           ...
# 129969    False
# 129970    False
# Name: country, Length: 129971, dtype: bool
# 此操作根据每个记录的国家/地区生成一系列真/假布尔值。然后可以在loc内部使用此结果来选择相关数据：

reviews.loc[reviews.country == 'Italy']
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	        Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6	        Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129961	Italy	Intense aromas of wild cherry, baking spice, t...	NaN	90	30.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	COS 2013 Frappato (Sicilia)	Frappato	COS
# 129962	Italy	Blackberry, cassis, grilled herb and toasted a...	Sàgana Tenuta San Giacomo	90	40.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	Cusumano 2012 Sàgana Tenuta San Giacomo Nero d...	Nero d'Avola	Cusumano
# 19540 rows × 13 columns

# This DataFrame has ~20,000 rows. The original had ~130,000. That means that around 15% of wines originate from Italy.

# 我们还想知道哪些比平均水平要好。葡萄酒被评为80到100分，所以这可能意味着葡萄酒至少积累了90分。
# We can use the ampersand (&) to bring the two questions together:

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 120	    Italy	Slightly backward, particularly given the vint...	Bricco Rocche Prapó	92	70.0	Piedmont	Barolo	NaN	NaN	NaN	Ceretto 2003 Bricco Rocche Prapó (Barolo)	Nebbiolo	Ceretto
# 130	    Italy	At the first it was quite muted and subdued, b...	Bricco Rocche Brunate	91	70.0	Piedmont	Barolo	NaN	NaN	NaN	Ceretto 2003 Bricco Rocche Brunate (Barolo)	Nebbiolo	Ceretto
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129961	Italy	Intense aromas of wild cherry, baking spice, t...	NaN	90	30.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	COS 2013 Frappato (Sicilia)	Frappato	COS
# 129962	Italy	Blackberry, cassis, grilled herb and toasted a...	Sàgana Tenuta San Giacomo	90	40.0	Sicily & Sardinia	Sicilia	NaN	Kerin O’Keefe	@kerinokeefe	Cusumano 2012 Sàgana Tenuta San Giacomo Nero d...	Nero d'Avola	Cusumano
# 6648 rows × 13 columns

# 假设我们会买任何意大利产的酒或评级高于平均水平的酒。为此，我们使用pipe(|)：

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	        Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6	        Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit
# 61937 rows × 13 columns

# 熊猫有几个内置的条件选择器，我们将在这里突出显示其中两个。

# 第一个是isin。isin 允许您选择其值“在”值列表中的数据。
# 例如，以下是我们如何使用它来选择仅来自意大利或法国的葡萄酒：
reviews.loc[reviews.country.isin(['Italy', 'France'])]
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 0	        Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
# 6     	Italy	Here's a bright, informal red that opens with ...	Belsito	87	16.0	Sicily & Sardinia	Vittoria	NaN	Kerin O’Keefe	@kerinokeefe	Terre di Giurfo 2013 Belsito Frappato (Vittoria)	Frappato	Terre di Giurfo
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit
# 41633 rows × 13 columns

# 第二个是isnull(和它的同伴not null)。这些方法使您可以高亮显示为(或不为)空(NaN)的值。
# 例如，要过滤掉数据集中没有价格标签的葡萄酒，我们将执行以下操作：

reviews.loc[reviews.price.notnull()]
#           country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
# 1	        Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
# 2	        US	Tart and snappy, the flavors of lime flesh and...	NaN	87	14.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Rainstorm 2013 Pinot Gris (Willamette Valley)	Pinot Gris	Rainstorm
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 129969	France	A dry style of Pinot Gris, this is crisp with ...	NaN	90	32.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Marcel Deiss 2012 Pinot Gris (Alsace)	Pinot Gris	Domaine Marcel Deiss
# 129970	France	Big, rich and off-dry, this is powered by inte...	Lieu-dit Harth Cuvée Caroline	90	21.0	Alsace	Alsace	NaN	Roger Voss	@vossroger	Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...	Gewürztraminer	Domaine Schoffit
# 120975 rows × 13 columns

# 设定 data
# Going the other way, assigning data to a DataFrame is easy. You can assign either a constant value:

reviews['critic'] = 'everyone'
reviews['critic']
# 0         everyone
# 1         everyone
#             ...
# 129969    everyone
# 129970    everyone
# Name: critic, Length: 129971, dtype: object
# Or with an iterable of values:

reviews['index_backwards'] = range(len(reviews), 0, -1)
# reviews['index_backwards']
# 0         129971
# 1         129970
#            ...
# 129969         2
# 129970         1
# Name: index_backwards, Length: 129971, dtype: int64