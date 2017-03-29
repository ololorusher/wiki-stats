#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            readsplit=f.read().split()
            (n, _nlinks) = [int(x) for x in (readsplit[0], readsplit[1])]
            
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

           #read from file
            i=5
            j=0
            while i<len(readsplit):
                k=i+int(readsplit[i])
                tmp=[int(x) for x in readsplit[i+1:k+1]]
                for s in tmp:
                    self._links[j] = s
                    j+=1
                i=k+4

            j=1
            i=3
            f=0
            self._offset[0]=0
            while j<=n:
                self._offset[j]=self._offset[j-1]+int(readsplit[i+2])
                self._titles.append(readsplit[i-1])
                self._redirect[f] =int(readsplit[i+1])
                self._sizes[f]=int(readsplit[i])
                f+=1
                i+= int(readsplit[i+2])
                j+=1

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return len(self.get_links_from(_id))

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        pass

    def get_number_of_pages(self):
        pass

    def is_redirect(self, _id):
        pass

    def get_title(self, _id):
        pass

    def get_page_size(self, _id):
        pass


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы