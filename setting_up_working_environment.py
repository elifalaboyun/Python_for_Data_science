print("hello world")

#################################################
#Virtual Environment(sanal ortam) ve package management (paket yönetimi)
##########################################

# Sanal ortamların listelenmesi:
 # conda env list


 #sanal ortam oluşturma :
 # conda create -n myenv

 #sanal ortamı aktif etme:
#conda activate my_env

#yüklü paketlerin listelenmesi
# conda list

#paket yükleme:
#conda install numpy

# aynı anda birden fazla paket yükleme
# conda install numpy scipy pandas

# paket silme:
# conda remove package_name


# belirli bir versiyona göre paket yükleme
# conda install numpy=1.20.1

# paket yükseltmek için :
# conda upgrade conda

# bütün kütüphaneleri yükseltmek için
# conda upgrade -all


# pip: pypi (python package index) paket yönetim aracı paket yükleme:
# pip install paket_adi

# paket yükleme versiyona göre:
# pip install pandas==1.2.1

#paket listesini export edip başka bir pcye felan aktarmak için
# conda env export > environment.yaml 