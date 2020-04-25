# 1. Title

Angular has a Title service in @angular/platform-browser. We just inject the Title service in our components and use the setTitle method to set the title.

    import { Title } from "@angular/platform-browser"@Component({  
        ...  
    })  
    export class LoginComponent implements OnInit {  
        constructor(private title: Title) {} ngOnInit() {  
            title.setTitle("Login")  
        }  
    }

# 2. Meta

Our Angular app renders things that are mostly from the index.html. The meta tags our app will have is the one set in the index.html. Angular has a Meta service in the @angular/platform-browser that enables us to set meta tags from our components.

It is very easy to use, just import Meta from@angular/platform-browser and inject it in our component.

    import { Meta } from "@angular/platform-browser"@Component({  
        ...  
    })  
    export class BlogComponent implements OnInit {  
        constructor(private meta: Meta) {} ngOnInit() {  
            meta.updateTag({name: "title", content: ""})  
            meta.updateTag({name: "description", content: "Lorem ipsum dolor"})  
            meta.updateTag({name: "image", content: "./assets/blog-image.jpg"})  
            meta.updateTag({name: "site", content: "My Site"})  
        }  
    }

# 3. Override Template interpolation


The start is  `{{`  and the end is  `}}`. If we place a property member in between them it will be rendered on browser DOM.

    @Component({  
        interpolation: ["((","))"]  
    })  
    export class AppComponent {}
    
    The interpolation to use in the AppComponent’s template will be  `"(())"`  no longer  `"{{}}"`.
    
    @Component({  
        template: `  
            <div>  
                ((data))  
            </div>  
        `,  
        interpolation: ["((","))"]  
    })  
    export class AppComponent {  
        data: any = "dataVar"  
    }

On rendering  `"dataVar"`  will be rendered in place of  `((data))`.

# 4. Location

We inject the Location service from the CommonModule to use it.

    import { Location } from "@angular/common"@Component({  
        ...  
    })  
    export class AppComponent {  
        constructor(private location: Location) {} navigateTo(url) {  
            this.location.go(url)  
        } goBack() {  
            location.back()  
        } goForward() {  
            location.forward()  
        }  
    }

# 5. DOCUMENT

 It provides DOM operations in an environment-agnostic way.

Note: Document might not be available in the Application Context when Application and Rendering Contexts are not the same (e.g. when running the application into a Web Worker).

Let’s say we have an element in our html:

    <canvas id="canvas"></canvas>

We can get hold of the canvas HTMLElement by injecting DOCUMENT:

    @Component({})  
    export class CanvasElement {  
        constructor(@Inject(DOCUMENT) _doc: Document) {}  
    }
    
    We can then get the HTMLElement of canvas by calling getElementById()
    
    @Component({})  
    export class CanvasElement {  
        constructor(@Inject(DOCUMENT) _doc: Document) {} renderCanvas() {  
            this._doc.getElementById("canvas")  
        }  
    }

We can safely do this using ElementRef and template reference but you got the idea.

# 6. @Attribute decorator

We have used mainly: Component, Module, Directive decorators in our Angular app.

We have this Attribute decorator, which enables us to pass static string without a cost at performance by eliminating change detection check on it.

The values of Attribute decorator are checked once and never checked again. They are used similarly to @Input decorator:

    @Component({  
        ...  
    })  
    export class BlogComponent {  
        constructor(@Attribute("type") private type: string ) {}  
    }

# 7. HttpInterceptor


In rare cases, interceptors may wish to completely handle a request themselves, and not delegate to the remainder of the chain. This behavior is allowed.

HttpInterceptor can be used in:

-   Authentication
-   Caching
-   Fake backend
-   URL transformation
-   Modifying headers

It is simple to use, first create a service and implement the HttpInterceptor interface.

    @Injectable()  
    export class MockBackendInterceptor implements HttpInterceptor {  
        constructor() {} intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {  
            ...  
        }  
    }

Then, insert it in your main module:

    @NgModule({  
        ...  
        providers: [  
            {  
                provide: HTTP_INTERCEPTORS,  
                useClass: MockBackendInterceptor,  
                multi: true  
            }  
        ]  
        ...  
    })  
    export class AppModule {}

# 8. AppInitializer


`APP_INITIALIZER`: A function that will be executed when an application is initialized.

It is easy to use. Let’s we want this runSettings function to be executed on our Angular app startup:

    function runSettingsOnInit() {  
        ...  
    }

We go to our main module, AppModule and add it to providers section in its NgModule decorator:

    @NgModule({  
        providers: [  
            { provide: APP_INITIALIZER, useFactory: runSettingsOnInit }  
        ]  
    })

# 9. Bootstrap Listener

Just like AppInitializer, Angular has a feature that enables us to listen on when a component is being bootstrapped. It is the  `APP_BOOTSTRAP_LISTENER`.

    @NgModule({  
        {  
            provide: APP_BOOTSTRAP_LISTENER, multi: true,   
            useExisting: runOnBootstrap  
        }  
        ...  
    })  
    export class AppModule {}

# 10. NgPlural

Pluralization is a problem in its sphere. We need to always correctly define grammar in our apps based on the singular/plural value. Some websites use the (s). Like:

To use this directive you must provide a container element that sets the  `[ngPlural]`  attribute to a switch expression. Inner elements with a  `[ngPluralCase]`  will display based on their expression:

<p [ngPlural]="components">  
    <ng-template ngPluralCase="=1">1 component removed</ng-template>      
    <ng-template ngPluralCase=">1">{{components}} components removed </ng-template>      
</p>

See, we have used NgPlural directive to remove the  `(s)`  when displaying number of "components removed". It will display:

    // if 1 component  
    1 component removed// if 5 components  
    5 components removed
