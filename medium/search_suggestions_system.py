class Solution:
    def suggestedProducts(self, products, searchWord: str):

        products.sort()
        results = []
        for i in range(0, len(searchWord)):
            word = searchWord[0:i+1]

            inner = []

            l = 0
            h = len(products)
            while(l < h):
                m = (l + h)//2
                print(l, m, h)
                if word > products[m]:
                    print(word, products[m])

                    print("what")
                    l = m + 1
                elif word < products[m]:
                    print(word, products[m])
                    print('pls')
                    h = m - 1

                else:
                    l = m
                    break

            numIter = min(3, len(products)-l)

            for j in range(0, numIter):
                if word != products[l+j][0:i+1] or len(products[l+j]) < len(word):
                    break
                inner.append(products[l+j])
            results.append(inner)

        return results


if __name__ == "__main__":
    s = Solution()
    prod = ["bags", "baggage", "banner", "box", "cloths"]
    searchword = "bags"
    print(s.suggestedProducts(prod, searchword))
