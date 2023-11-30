# from blog.models import Author, Blog    # blog papkasinnan classlari import etdik
# a1 = Author.objects.all()  # all() funksiyasi author classindaki butun objectleri cagirmag ucundur, cavabi a1 - e beraber etdik
# a1    # a1 - i cagiririg
# <QuerySet [<Author: Rick Sanchez>, <Author: Morty Smith>, <Author: Jerry Smith>]>   # ve bize Query set qaytarir, icinde butun elementler var


# >>> a1.filter(full_name='Rick Sanchez')     # filter() funksiyasi verilene uygun seti filterleyir, bos filter() all() - a beraberdir
# <QuerySet [<Author: Rick Sanchez>]>

# a1.filter(full_name__icontains='rick')    # icontains() funksiyasi verilen soz her hansi bir deyere uygundursa onu qaytarir, icontains() herflerin boyuk ve ya kicik olmasinnan asili deyil, eyni seyleri eden icontain ise herflerin boyuk ve kisik olmasindan asilidir
# <QuerySet [<Author: Rick Sanchez>]>       # Bu funksiyalar istifade edilerken keyword - den sonra 2 alt xett, sonra ise funksiyanin adi yazilir

# rick = a1.filter(full_name__icontains='rick')   # Query seti rick deyisenine beraber etdik
# >>> rick
# <QuerySet [<Author: Rick Sanchez>]> 
# >>> rick.full_name
# AttributeError: 'QuerySet' object has no attribute 'full_name'    # rick deyiseni Query sete beraber oldugu ucun birbasa elementi bir basa ordan ceke bilmirik istifade ede bilmirik
# rick[0].full_name    # Query setin icindeki elementler hemde listin icinde verilir, ona gorede elementi indexe gore goturub funksiyani ele istifade edirik
# 'Rick Sanchez'

# rick.first()   # first() - funksiyasi ilk yerde duran (0-ci index-de ki) elementi verir
# <Author: Rick Sanchez>
# >>> rick.first().full_name
# 'Rick Sanchez'

# rick.last()    # last() - funksiyasi son yerde duran funksiyani qaytarir
# <Author: Rick Sanchez>
# >>> rick.last().full_name  
# 'Rick Sanchez'


# all() ve filter() coxluq(QuerySet), first() ve last() ise obyekt qaytarir


# startswith() - her hansi bir string bu funksiyanin arqumentinde verilen herif(ve ya sozun baslangicindaki herflerle) baslayirsa funksiya True qaytarir
# endswith() - startswith - in sozun sonu ucun olanidir

# names = ['Rick Sanchez']
# authors = Author.objects.filter(full_name__in=names)  # in() - funksiyasi beraber edildiyi coxulugun elementlerini, filter() olunan setde axtarmag ucundur setde axtarmag ucundur
# >>> authors
# <QuerySet [<Author: Rick Sanchez>]>         # Author - un icindeki, hemde  names listinde olannari qaytardi
# in() - hemise coxluga beraber edilir(set,list,tuple ve s.)


# authors = Author.objects.filter(age__gt=5)    # gt - funksiyasi(greater than) beraber edildiyi deyerden boyuk olannlari filtirlemek ucundur
# >>> authors
# <QuerySet [<Author: Morty Smith>]>

# authors = Author.objects.filter(age__gte=14)  # gte - (grater than or equal) gt funksiyasi kimidir amma deyere beraber olannarida verir
# >>> authors
# <QuerySet [<Author: Morty Smith>]>

# lt(less than) ve lte(less than or equal) da eyni cur isleyir

# authors = Author.objects.get(age__gte=14)     # get() de filter() kimidir, ancag  coxlug yox element qaytarir, ve yalniz bir cavab qaytarir, uygun gelen 2 ve daha cox cavab olarasa error verir
# >>> authors
# <Author: Morty Smith>

# get() - den setde olmayan object istense error verir ve kod qirilir, buna gorede asagidakini istifade etmek daha serfelidir
# authors = Author.objects.filter(age__gte=15).first()   # filterleyib birinci elementi goturende verilen obyekt movcud olmasa bele, error yox bosluq qaytarir



# authors = Author.objects.exclude(age__gte=15)  # exclude() - filter()-in tersidir, verilene uygun olmayanlari qaytarir
# >>> authors
# <QuerySet [<Author: Jerry Smith>, <Author: Morty Smith>]>


# a2 = Author.objects.create(full_name='Adolf Hitler', age=55)    # create() - yeni bir obyekt teyin etmek ucundur(adminden yox shellden)
# >>> a2
# <Author: Adolf Hitler>

# authors.update(age=18)     # QuerySet qebul edir ve elementlerin hamisini deysir
# 4     # (elementlerin sayi)
# >>> authors
# <QuerySet [<Author: Jerry Smith>, <Author: Morty Smith>, <Author: Rick Sanchez>, <Author: Adolf Hitler>]>
# >>> authors.first()
# <Author: Rick Sanchez>
# >>> authors.first().age
# 18



# a3 = authors.first()
# >>> a3
# <Author: Rick Sanchez>
# >>> a3.age = 50     # her hansi bir deyeri deyismek ucun, onu yeni deyere beraber etmek,
# >>> a3.save         # ve sonra mutleq save() funksiyasini istifade etmek lazimdir(oncesinde ise yeni deyere beraber etmek lazimdir(a3-e beraber etdiyimiz kimi))
# <bound method Model.save of <Author: Rick Sanchez>>
# >>> a3.age
# 50

# a3.delete()     # delete() - hemin authoru silmek ucun istifade etdik
# (1, {'blog.Author': 1}


# from django.db.models import Q         # Q or vezifesi gorur, import plunmalidir
# >>> Author.objects.filter(full_name__icontains='y', age__lt=56)    # burada her iki serte uygun olan qaytarilir
# <QuerySet [<Author: Jerry Smith>]>
# >>> Author.objects.filter(Q(full_name__icontains='y') | Q(age__lt=56))    # Burada ise ikisinden birini odeyenler
# <QuerySet [<Author: Jerry Smith>, <Author: Adolf Hitler>, <Author: Morty Smith>]>


# Blog.objects.filter(author__age__gt=50)        # Blogu yazarinin yasina gore filterliyirik, bize yazarinin yasi 50-den boyuk olan blog qaytarir 
# <QuerySet [<Blog: Lorem ipsum is placeholder text commonly used in the graphic>]>

# authors.first().blogs.first()    # Birinci authorun birinci blogunu goturmek ucun(QuerySet qaytarir)
# <Blog: Lorem ipsum is placeholder text commonly used in the graphic>



# a = Author.objects.all()
# >>> a
# <QuerySet [<Author: Jerry Smith>, <Author: Adolf Hitler>, <Author: Morty Smith>]>     # Normalda QuerySet - de objectleri ilk teyin olunandan sonrakine dodru duzur(ilk teyin oluanin id-si 1, ikincinin 2 ve s.)
# >>> a = Author.objects.all().order_by('-id')     # order_by('') funksiyasi elementleri verilen sertlere uygun duzmek ucundur, burada '-id' elementlerin son teyin olunandan ilkine dogru duzmek ucundur
# >>> a
# <QuerySet [<Author: Adolf Hitler>, <Author: Jerry Smith>, <Author: Morty Smith>]>


# order_by('') tarix, yas ve basqa gostericilere uygun elementleri duzmek ucundur

# a = Author.objects.all().order_by('age')
# >>> a
# <QuerySet [<Author: Jerry Smith>, <Author: Adolf Hitler>, <Author: Morty Smith>]>
# a = Author.objects.all().order_by('-age')
# >>> a
# <QuerySet [<Author: Morty Smith>, <Author: Jerry Smith>, <Author: Adolf Hitler>]>
