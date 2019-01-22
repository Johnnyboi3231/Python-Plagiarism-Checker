'''
 The MIT License(MIT)
 
 Copyright(c) 2016 Copyleaks LTD (https://copyleaks.com)
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''

from copyleaksSdk.models.types.eDomainsFilteringMode import eDomainsFilteringMode
class Filters:
    '''
    Customizable filters

    Attributes:
    -----------
        idenitcalEnabled : boolean
            Enable/disable identical matches
        minorChangedEnabled : boolean
            Enable/disable minor changes matches
        relatedMeaningEnabled : boolean
            Enable/disable related meaning matches
        minCopiedWords : int
            Set the minimum copied words to be considered as plagiarized content 
        safeSearch : boolean
            When set to true the result will not include explicit results.
            Safe search is not 100% accurate but it can help avoid explicit and inappropriate search results
        domains : list
            A list of domain to include or exclude from sources
        domainsMode : eDomainsFilteringMode
            Treat `domains` as include or exclude list
    '''
    def __init__(self, idenitcalEnabled=True, minorChangedEnabled=True, relatedMeaningEnabled=True, minCopiedWords=None, 
                safeSearch=False, domains=[], domainsMode=eDomainsFilteringMode.WhiteList):
        self.idenitcalEnabled = idenitcalEnabled
        self.minorChangedEnabled = minorChangedEnabled
        self.relatedMeaningEnabled = relatedMeaningEnabled
        self.minCopiedWords = minCopiedWords
        self.safeSearch = safeSearch
        self.domains = domains
        self.domainsMode = domainsMode