#include <iostream>
#include <sstream>
#include <type_traits>
#include <vector>


// https://stackoverflow.com/a/59511109/6304872
template< class, class = std::void_t<> >
struct has_vt : std::false_type { };
template< class T >
struct has_vt<T, std::void_t<typename T::value_type>> : std::true_type { };
template <typename T, typename Enable = void> struct inner;
template <typename T> struct inner<T, typename std::enable_if<!has_vt<T>::value>::type> {
    using vt = T;
};
template <typename T> struct inner<T, typename std::enable_if<has_vt<T>::value>::type> {
    using vt = typename inner<typename T::value_type>::vt;
};


template<class T>
class Fenwick {
public:
    using value_type = T;
    template<class...Sizes>
    Fenwick(size_t size, Sizes ...sizes) : tree(size, T(sizes...)) {};
    Fenwick(size_t size) : tree(size) {};

    template<class...Xs>
    void add(inner<T>::vt delta, size_t index, Xs ...xs){
        while (index < tree.size()) {
            if constexpr (sizeof...(Xs)) {
                tree[index].add(delta, xs...);
            } else{
                tree[index] += delta;
            }
            index |= index + 1;
        }
    }

    template<class...Xs>
    inner<T>::vt prefix(size_t index, Xs ...xs) const {
        index += 1;
        typename inner<T>::vt accumulator = 0;
        while (index > 0) {
            index -= 1;
            if constexpr (sizeof...(Xs)){
                accumulator += tree[index].prefix(xs...);
            } else {
                accumulator += tree[index];
            }
            index &= index + 1;
        }
        return accumulator;
    }
private:
    std::vector<T> tree;
};


using Fenwick3D = Fenwick<Fenwick<Fenwick<int>>>;

int cube(const Fenwick3D& tree, int x1, int y1, int z1, int x2, int y2, int z2){
    return (
        tree.prefix(x2, y2, z2)        
        - tree.prefix(x1 - 1, y2, z2)
        - tree.prefix(x2, y1 - 1, z2)
        - tree.prefix(x2, y2, z1 - 1)
        + tree.prefix(x2, y1 - 1, z1 - 1)
        + tree.prefix(x1 - 1, y2, z1 - 1)  
        + tree.prefix(x1 - 1, y1 - 1, z2)
        - tree.prefix(x1 - 1, y1 - 1, z1 - 1)
    );
}


int main(){
    using namespace std;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    ostringstream ss;
    Fenwick3D tree(n, n, n);
    while (true){
        int mode;
        cin >> mode;
        if (mode == 3){
            break;
        }
        if (mode == 1){
            int x, y, z, k;
            cin >> x >> y >> z >> k;
            tree.add(k, x, y, z);
        }
        if (mode == 2){
            int x1, y1, z1, x2, y2, z2;
            cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
            ss << cube(tree, x1, y1, z1, x2, y2, z2) << "\n";
        }
    }
    cout << ss.str();
}